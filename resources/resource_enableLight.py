#template voor API
from flask_restful import Resource

#file waarin de functie is geschreven importeren
import mesh_manager

#Resource in parameters van class zodat het via de API kan worden opgeroepen
class enable(Resource):

#definieer de class om bij de functie te komen. 
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager() 

#roep functie aan met de nodige parameter(S).
    def get(self):
        self.mesh_manager.enable_light()
        return 