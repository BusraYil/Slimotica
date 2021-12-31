import time

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


class MeshManager(metaclass=Singleton):
    def __init__(self):
        print('MeshManager has been made')
        DATABASE_PATH = 'database/example_database.json'
        DEVICE = 'COM14'
        self.db = MeshDB(DATABASE_PATH)
        self.device = Interactive(Uart(port=DEVICE, baudrate=115200, device_name=DEVICE))
        self.provisioner = Provisioner(self.device, self.db)


    def provision_device(self, name: str):
        self.provisioner.scan_start()
        time.sleep(5)
        self.provisioner.scan_stop()
        self.provisioner.provision(name=name)
    

    def configure_device(self, key_handle: str, address_handle: str): #deze 2 waardes moeten uit logfile worden gehaald
        self.cc = ConfigurationClient(self.db)
        device.model_add(self.cc)
        self.cc.publish_set(key_handle = key_handle, address_handle = address_handle)
        self.cc.composition_data_get()


    # def bind_on_off_server(self, element_address: str, appkey_add: str,  model_id: str): #modelID moet uit die compositiondata eruit worden gehaad
    #     self.cc.appkey_add(appkey_add =appkey_add) #is dit wel zo handig? we gebruiken toch 1 groep
    #   #  self.cc.model_app_bind(element_address= element_address, appkey_add =appkey_add, model_id=model_id)    #deze 
    #     self.cc.model_app_bind(self.db.nodes[0].unicast_address, appkey_add=appkey_add, mt.ModelId(model_id)    #of deze?
    #     #index van nodes moet worden opgehoogd naarmate er meer nodes worden toegevoegd (provisionen van nieuw devicd)

    #     gc1 = GenericOnOffClient()
    #     device.model_add(self.node1)

    #     self.node1.publish_set(key_handle, address_handle) #in het document staat er wat andets

    

    # def add_subscription_adress(self):
    #     self.cc.model_subscription_add(element_address, address, model_id)


    # def enable_light(self):
    #     self.node1.set(True)
    
    # def disable_light(self):
    #     self.node1.set(False)