import json
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

class Singleton(type): #zorgt ervoor dat er slechts 1 object van zijn soort bestaat en het een enkel toegangspunt biedt voor alle andere code
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Node:
    def __init__(self, name = "", devkey_handle = 0, address_handle = 0, compdata_received = False, onoff = -1):
        self.name = name
        self.devkey_handle = devkey_handle
        self.address_handle = address_handle
        self.compdata_received = compdata_received
        self.onoff = onoff

class MeshManager(metaclass=Singleton):
    def __init__(self):
        print('MeshManager has been made')

        DATABASE_PATH = 'database/example_database.json'
        DEVICE = 'COM14'
        self.LOGFILE_PATH = 'log\output.log'
        self.SERVER_AMOUNT = 3

        self.nodes = []
        self.present_nodes = 0
        self.gc = []

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
        self.provisioner.scan_stop()
        self.provisioner.provision(name=name)

        time.sleep(10)

        # Obtain devkey and address handle
        devkey = self.get_handle("devkey_handle")
        address = self.get_handle("address_handle")

        self.nodes.append( Node(name = name, devkey_handle = devkey, address_handle = address) )

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
        

    def configure_device(self, node : int, type : int):
        self.cc.publish_set(key_handle = self.nodes[node].devkey_handle, address_handle = self.nodes[node].address_handle)
        time.sleep(1)

        if not self.nodes[node].compdata_received:
            self.cc.composition_data_get()
            time.sleep(2)
            self.nodes[node].compdata_received = True
            
        model = 0

        if type:
            model = 0x1001
        else:
            model = 0x1000

    # def bind_on_off_server(self, element_address: str, appkey_add: str,  model_id: str): #modelID moet uit die compositiondata eruit worden gehaad
        self.cc.appkey_add(0)
        time.sleep(1)
        self.cc.model_app_bind(self.db.nodes[node].unicast_address, 0, mt.ModelId(model))    
        time.sleep(1)

        self.gc[node].publish_set(0, self.nodes[node].address_handle)

        self.present_nodes += 1
    
        if type:
            self.cc.model_publication_set(self.db.nodes[node].unicast_address + 1, mt.ModelId(0x1001), mt.Publish(self.db.nodes[0].unicast_address, index=0, ttl=1))
        time.sleep(1)

    # def add_subscription_adress(self):
    #     self.cc.model_subscription_add(element_address, address, model_id)


    def set_light(self, index : int, state : bool):
        if index >= 0 and index < self.present_nodes:
            self.gc[index].set(state)
            time.sleep(1)