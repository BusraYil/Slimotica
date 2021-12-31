from flask_restful import Resource
import convert_log


class convertLog(Resource):
    def __init__(self):
        self.convert_log = convert_log.Logdocument()
       

    def get(self):
        self.convert_log.main()
        return 