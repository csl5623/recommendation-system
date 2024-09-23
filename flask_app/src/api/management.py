from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.file import *

class Init(Resource):
    def post(self):
        