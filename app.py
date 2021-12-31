from flask import Flask
from flask_restful import Api

from resources.resource_provision import Provision
# from resources.resource_convertLog import convertLog

app = Flask(__name__)
api = Api(app)

api.add_resource(Provision, "/provision")
#api.add_resource(convertLog, "/logfile")
#api.add_resource(enable, "/enableLight")

with open('log\output.log', 'w'):
    pass

if __name__ == '__main__':
    app.run(debug=True)