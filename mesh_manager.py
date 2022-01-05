import time
import interactive_pyaci

from mesh import access
from mesh.provisioning import Provisioner, Provisionee
from mesh import types as mt
from mesh.database import MeshDB
from models.config import ConfigurationClient
from models.generic_on_off import GenericOnOffClient
from aci.aci_uart import Uart
from interactive_pyaci import Interactive
from models.config import ConfigurationClient
from mesh_exceptions import meshExcep

class Singleton(type): #zorgt ervoor dat er slechts 1 object van zijn soort bestaat en het een enkel toegangspunt biedt voor alle andere code
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Node:
    def __init__(self, index = 0, name = "", type = 0, devkey_handle = 0, address_handle = 0, 
                initialised = False, configured = False, models_bound = [False, False, False], onoff = 0):
        self.index = index
        self.name = name
        self.type = type
        self.devkey_handle = devkey_handle
        self.address_handle = address_handle
        self.initialised = initialised
        self.configured = configured
        self.models_bound = models_bound
        self.onoff = onoff

class MeshManager(metaclass=Singleton):
    def __init__(self):
        print('MeshManager has been made')

        DATABASE_PATH = 'database/example_database.json'
        DEVICE = 'COM14'
        self.LOGFILE_PATH = 'log\output.log'
        self.SERVER_AMOUNT = 3

        self.nodes = []
        self.nodes_count = {}
        self.nodes_count["active"] = 0
        self.nodes_count["provisioned"] = 0
        self.nodes_count["server"] = 0
        self.nodes_count["client"] = 0

        self.gc = []
        self.meshExcep = meshExcep()
        self.db = MeshDB(DATABASE_PATH)
        self.device = Interactive(Uart(port=DEVICE, baudrate=115200, device_name=DEVICE))
        self.provisioner = Provisioner(self.device, self.db)
        self.cc = ConfigurationClient(self.db)
        self.device.model_add(self.cc)

        for x in range(self.SERVER_AMOUNT):
            self.gc.append( GenericOnOffClient() )
            self.device.model_add(self.gc[x])


    def provision_device(self, name: str):
        self.provisioner.scan_start()
        time.sleep(5)
        # if self.meshExcep.checkForUUID():
        self.provisioner.scan_stop()
        self.provisioner.provision(name=name)
        # else:
            # self.provisioner.scan_stop()

        if self.meshExcep.check_for_provisioning():
            pass
        else:
            self.meshExcep.wait_till_provisioned_succesfully()

        devkey = self.get_handle("devkey_handle")
        address = self.get_handle("address_handle")
        self.nodes.append( Node(index = self.nodes_count["provisioned"], name = name, devkey_handle = devkey, address_handle = address) )

        self.nodes_count["provisioned"] += 1
        self.nodes_count["active"] += 1

        time.sleep(1)


    def get_handle(self, name : str) -> int:
    
        out = 0

        with open(self.LOGFILE_PATH, 'r') as f:
            for line in f:
                if "INFO" in line:
                    if name in line:
                        index = line.index(name)
                        buffer = line[index + 16:]
                        out = int(buffer.split("}")[0]) 

        return out
        
    def get_nodeType(self) -> int:
        
        res = ""
        target = "modelId"

        with open('log\output.log', 'r') as f:
            for line in f:
                if (not "INFO" in line) and (not "DEBUG" in line):
                    if target in line:
                        index = line.index(target)
                        buffer = line[index + 11:]

                        if ("1001" in buffer) or ("1000" in buffer):
                            res = buffer.split('"')[0]

        if (res == "1001"):
            return 1
        elif (res == "1000"):
            return 0
        else:
            return -1


    def get_nextServer(self, count : int) -> int:
        cnt = 0
        for node in self.nodes:
            if (node.type == 0):
                    cnt += 1
                    if (cnt > count):
                        return node.index 


    def configure_device(self, node = -1):

        # Select first unconfigured node in nodes list if node argument is not specified
        if (node == -1):
            for n in self.nodes:
                if not n.configured:
                    node = n.index
                    n.configured = True
                    break

        # Set configuration client publication address to selected node
        self.cc.publish_set(key_handle = self.nodes[node].devkey_handle, address_handle = self.nodes[node].address_handle)
        time.sleep(1)

        # Check if device has been initialised already
        if not self.nodes[node].initialised:
        
            self.cc.composition_data_get()
            time.sleep(3)

            # Check if composition data has been received
            # if self.meshExcep.check_for_model():
            self.nodes[node].initialised = True
            self.nodes[node].type = self.get_nodeType()

            # Add appKey to device
            self.cc.appkey_add(0)
            time.sleep(1)

            type = self.nodes[node].type

            if (type == 0):
                self.gc[ self.nodes_count["server"] ].publish_set( 0, self.nodes[node].address_handle )
                self.nodes_count["server"] += 1

                # Bind appKey to server model instance
                self.cc.model_app_bind(self.db.nodes[node].unicast_address, 0, mt.ModelId(0x1000))

            elif (type == 1):
                self.nodes_count["client"] += 1

                # Bind appKey to client model instances
                for x in range (3):
                    self.cc.model_app_bind(self.db.nodes[node].unicast_address + x + 1, 0, mt.ModelId(0x1001))
                    time.sleep(1) 
            else:
                print("Invalid type")
                return

        time.sleep(1)

        count = 0

        type = self.nodes[node].type

        if (type == 1):
            for bound in self.nodes[node].models_bound:
                if (not bound) and (count < self.nodes_count["server"]): 

                    index = self.get_nextServer(count)
                    self.cc.model_publication_set(self.db.nodes[node].unicast_address + count + 1, 
                                                  mt.ModelId(0x1001), 
                                                  mt.Publish(self.db.nodes[index].unicast_address, index=0, ttl=1))
                    self.nodes[node].models_bound[count] = True
                    count += 1                                                  
                    time.sleep(1) 
        elif (type != 0):
            print("Invalid type")
            return


    def set_light(self, index : int, state : int):
        if index >= 0 and index < self.nodes_count["active"]:
            self.gc[index].set(state)
            time.sleep(1)