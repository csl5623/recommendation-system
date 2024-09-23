from flask import Flask
from Flask_RESTful import Resource, Api


from api.management import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init')


if __name__ == '__main__':
    
    app.run(debug=True)