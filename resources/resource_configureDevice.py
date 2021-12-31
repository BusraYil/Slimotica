#template voor API
from flask_restful import Resource

#file waarin de functie is geschreven importeren
import mesh_manager
import convert_log

#Resource in parameters van class zodat het via de API kan worden opgeroepen
class Scan(Resource):

#definieer de class om bij de functie te komen. 
    def __init__(self):
        self.mesh_manager = mesh_manager.MeshManager() 
        self.convert_log = convert_log.Logdocument()

#roep functie aan met de nodige parameter(S). 
    def get(self):
        self.mesh_manager.configure_device(convert_log.parse_devkey, convert_log.parse_addrehandle) #weet niet of dit zo kan
        return 