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
        names = { 
            "index": []
        }

        print(len(self.mesh_manager.nodes))

        for x in self.mesh_manager.nodes:
            names["index"].append(x.index)

        return names