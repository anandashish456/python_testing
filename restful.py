#!/usr/bin/env python

import cx_Oracle
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"name":"Ashish"}

    def post(self):
        some_json = request.get_json()
        return {"your_json":some_json}


class Multi(Resource):
    def get(self, num2):
        return {"result":num2*10}


class FetchDBDetails(Resource):
    def get(self):
        db_sid = request.args.get('dbsid')
        print ("Yes: " + db_sid)
        db_host = "lnxdb-dev-vm-288"
        db_port = "1551"
        dsn_tns = cx_Oracle.makedsn(db_host, db_port, db_sid)
        dbconn = cx_Oracle.connect("tools_admin", "a1phabet", dsn_tns)
        cursor = dbconn.cursor()
        cursor.execute("select * from dual")
        dbname = cursor.fetchall()
        return {"name":[x[0] for x in dbname][0]}



api.add_resource(HelloWorld, '/testyourAPI/')
api.add_resource(Multi, '/multi/<int:num2>')
api.add_resource(FetchDBDetails, '/db')


if __name__ == '__main__':
    app.run(debug=True)
