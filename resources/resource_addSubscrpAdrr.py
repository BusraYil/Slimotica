#template voor API
from flask_restful import Resource

#file waarin de functie is geschreven importeren
import mesh_manager

#Resource in parameters van class zodat het via de API kan worden opgeroepen
class Scan(Resource):

#definieer de class om bij de functie te komen. voorbeeld zoals hieronder.
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager() 

#roep functie aan met de nodige parameter(S). Voorbeeld zoals hieronder.
    def get(self):
        self.mesh_manager.provision_device("light#1")  
        return 