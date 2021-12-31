from mesh.database import MeshDB
import time
from mesh.provisioning import Provisioner 
db = MeshDB("database/example_database.json")
print(db.provisioners)
# "device = d[0]",
p = Provisioner(device, db)
print('plug in server')
time.sleep(10)

