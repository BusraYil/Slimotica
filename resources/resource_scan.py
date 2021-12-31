from flask_restful import Resource
import mesh_manager


class Scan(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()


    def get(self):
        self.mesh_manager.provision_device("light#1")
        return 