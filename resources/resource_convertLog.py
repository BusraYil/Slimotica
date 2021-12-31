from flask_restful import Resource
import mesh_manager


class ConvertLog(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()

    def get(self):
        self.mesh_manager.get_handle("devkey_handle")
        return 