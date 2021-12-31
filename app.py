from flask import Flask
from flask_restful import Api

import argparse

from misc import restore_json, restore_log
from resources.resource_provision import Provision
# from resources.resource_convertLog import convertLog

# app = Flask(__name__)
# api = Api(app)

# api.add_resource(Provision, "/provision")
#api.add_resource(convertLog, "/logfile")
#api.add_resource(enable, "/enableLight")

# Argument parser
parser = argparse.ArgumentParser(description='Main app script')
parser.add_argument("--reset_json", type = bool, default = 0)
parser.add_argument("--reset_log", type = bool, default = 0)

args = parser.parse_args()

reset_json_val = args.reset_json
reset_log_val = args.reset_log

if __name__ == '__main__':
    # app.run(debug=True)
    if reset_json_val:
        restore_json()

    if reset_log_val:
        restore_log()
