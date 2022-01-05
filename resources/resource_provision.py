from flask_restful import Resource, reqparse
import mesh_manager

class Provision(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, default = '')
        args = parser.parse_args()
        name = args['name']

        if (name == ''):
            print("ERROR: Name is required")
            return

        self.mesh_manager.provision_device(name)
        self.mesh_manager.configure_device()
        return