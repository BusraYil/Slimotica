from flask_restful import Resource, reqparse
import mesh_manager
import colored

class ConfigureDevice(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('index', type = int, default = -1)
        args = parser.parse_args()
        index = args['index']

        if (index == -1):
            print("ERROR: Index is required")
            return

        self.mesh_manager.configure_device(index)
        return