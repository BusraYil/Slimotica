#template voor API
from flask_restful import Resource, reqparse

#file waarin de functie is geschreven importeren
import mesh_manager

#Resource in parameters van class zodat het via de API kan worden opgeroepen
class SetLight(Resource):

#definieer de class om bij de functie te komen. 
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager() 

#roep functie aan met de nodige parameter(S).
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('index', type = int, default = -1)
        parser.add_argument('state', type = int, default = -1)
        args = parser.parse_args()
        index = args['index']
        state = args['state']

        if (index == -1):
            print("ERROR: Index is required")
            return

        if (state == -1):
            print("ERROR: Sate is required")
            return
        elif (state != 0) and (state != 1):
            print("ERROR: Invalid state")
            return

        self.mesh_manager.set_light(index, state)
        return 