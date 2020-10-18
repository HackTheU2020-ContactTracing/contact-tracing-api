from flask import Flask, request
from flask_restful import Api, Resource
import mysql.connector

app = Flask(__name__)
api = Api(app)
cnx = mysql.connector.connect(user="arturo", password='password', host='localhost', database='covid')

class Covid(Resource):
    def get(self, id):
        return {"exposed": True}

    def put(self, id):
        print(request.form['id'])

api.add_resource(Covid, "/covid/<string:id>")

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=5000, debug=True)

