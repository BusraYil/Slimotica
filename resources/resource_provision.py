from flask_restful import Resource
import mesh_manager
import time

class Provision(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()


    def get(self):
        self.mesh_manager.provision_device("light#1")
        self.mesh_manager.configure_device(0, 0)

        print("Plugin client")
        time.sleep(10)

        self.mesh_manager.provision_device("switch#1")
        self.mesh_manager.configure_device(1, 1)        
        return 