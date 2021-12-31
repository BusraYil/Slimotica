from flask import Flask
from flask_restful import Api

from resources.resource_scan import Scan
from resources.resource_convertLog import convertLog

app = Flask(__name__)
api = Api(app)

api.add_resource(Scan, "/provision")
# api.add_resource(convertLog, "/logfile")
#api.add_resource(enable, "/enableLight")

if __name__ == '__main__':
    app.run(debug=True)