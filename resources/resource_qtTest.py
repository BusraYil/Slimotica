from flask_restful import Resource, reqparse
import mesh_manager
import random
from mesh_manager import Node
import json

class qtTest(Resource):
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager()

    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('string', type = str, default = '')
        # args = parser.parse_args()
        # name = args['string']

        self.mesh_manager.nodes.append( Node(index = random.randint(0, 100)) )
        nodes = { 
            "index": [],
            "name": [],
            "type": [],
            "state": []
        }

        # print(len(self.mesh_manager.nodes))

        # for x in self.mesh_manager.nodes:
        nodes["index"].extend( ["0", "1", "2", "3", "4", "5"] )
        nodes["name"].extend( ["Light 1", "Switch 1", "Light 2", "Light 3", "Switch 2", "Switch 3"] )
        nodes["type"].extend( ["0", "1", "0", "0", "1", "1"] )
        nodes["state"].extend( ["1", "0", "1", "1", "0", "0"] )
        nodes["used"].extend( ["1", "1", "1", "1", "1", "1"])

        return nodes