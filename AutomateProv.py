# __version__ = '1.0.0'

# import os
# import sys
# import time


# from flask import Flask
# from flask_restful import Api, Resource


# from mesh import access
# from mesh.provisioning import Provisioner, Provisionee
# from mesh import types as mt
# from mesh.database import MeshDB
# from models.config import ConfigurationClient
# from models.generic_on_off import GenericOnOffClient
# from aci.aci_uart import Uart
# from interactive_pyaci import Interactive
# from models.config import ConfigurationClient

# from serial import SerialException


# DEVICE = 'COM12'
# DATABASE_PATH = 'database/example_database.json'

# #db = MeshDB(DATABASE_PATH)
# app = Flask(__name__)
# api = Api(app)


# class MeshManager:
#    # def __init__(self, db):
#     #    self.db = db
    

#     def provision_device(self, name: str):
#         db = MeshDB(DATABASE_PATH)
#         try:
#             device = Interactive(Uart(port=DEVICE, baudrate=115200, device_name=DEVICE))
#         except SerialException as e:
#             print(f'Couldnt open {DEVICE}, {e}.')
#             quit()
#         p = Provisioner(device, db)
#         p.scan_start()
#         time.sleep(5)
#         p.scan_stop()
#         p.provision(name=name)
    

#     def configure_device(self, device_key: str):
#         cc = ConfigurationClient(db)
#         device.model(cc)


# class ProvisionResource(Resource):
#     def __init__(self):
#         self.meshManag = MeshManager(db)
    

#     def get(self, naam):
#         self.meshManag.provision_device(name=naam)
#        # self.meshManag.configure_device(device_key)
#         return f'Provisioned {naam}!'


# def main():
#     b = MeshDB(DATABASE_PATH)
#     a = MeshManager()
#     a.provision_device(name="Light Bulb1")
#     time.sleep(15)

# api.add_resource(ProvisionResource, '/provision/<naam>')


# if __name__ == '__main__':
#     main()
#     app.run(debug=True)



#------------------------------------------------------------------------------------------------------------#


__version__ = '1.0.0'

import os
import sys
import time
import logging


from mesh import access
from mesh.provisioning import Provisioner, Provisionee
from mesh import types as mt
from mesh.database import MeshDB
from models.config import ConfigurationClient
from models.generic_on_off import GenericOnOffClient
from aci.aci_uart import Uart
from interactive_pyaci import Interactive
from models.config import ConfigurationClient

from serial import SerialException


DEVICE = 'COM12'
DATABASE_PATH = 'database/example_database.json'
import json

#open Json file
#f = open(DATABASE_PATH)




class MeshManager:  #constructure
  # def __init__(self, db):
   #     self.db = db
       

    def provision_device(self, name: str):
        db = MeshDB(DATABASE_PATH)
        try:
            device = Interactive(Uart(port=DEVICE, baudrate=115200, device_name=DEVICE))
        except SerialException as e:
            print(f'Couldnt open {DEVICE}, {e}.')
            quit()
        p = Provisioner(device, db)
        p.scan_start()
        time.sleep(5)
        p.scan_stop()
        p.provision(name=name)



    def configure_device(self, device_key: str):
    
        cc = ConfigurationClient(db)
        device.model(cc)

        cc.publish_set(logging.key_handle, logging.device_key)
        cc.composition_data_get()
        time.sleep(10)
        cc.appkey_add(0)
        #cc.model_app_bind(element_address , appkey_index, model_id)
            
        print("provisioning server 1 is completed!")
        print("wait for next server")
        time.sleep(10)



def main():
    b = MeshDB(DATABASE_PATH)
    a = MeshManager()
    a.provision_device(name="Light Bulb1")
    time.sleep(15)
    a.configure_device(DATABASE_PATH ['deviceKey'])
    
    
    #provision_device.configure_device
    
    

if __name__ == '__main__':
    main()
















    #     def update_database(self):
    #     data = None
    #     with open(DATABASE_PATH) as f:
    #         data = f.read()
    #     try:
    #         self.data = json.loads(data)
    #         return
    #     except:
    #         index = data.rfind(',')
    #         data = data[0 : index] + data[index + 1]
    #     self.data = json.loads(data)


    
    # def is_network_empty(self) -> bool:
    #     self.update_data()
    #     try:
    #         if len(self.update_data['nodes']) > 0:
    #             return False
    #         return True
    #     except KeyError:
    #         return True
