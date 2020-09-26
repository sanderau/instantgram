#!/usr/bin/python3.8

import flask
import mysql.connector
import os

#config and set up flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#get those env vars, so you people github cant hurt me
mysql_root_password = os.environ['MYSQL_ROOT_PASSWORD']
mysql_user = os.environ['MYSQL_USER']
mysql_host = os.environ['MYSQL_HOST']
mysql_db = os.environ['MYSQL_DB']

#get database connection values
config = { 
	'user': mysql_user,
	'password': mysql_root_password,
	'host': mysql_host,
	'database': mysql_db
}

cnx = mysql.connector.connect(**config)

@app.route('/', methods=['GET'])
def home():
	return "<h1> Hello World! </h1>"

# run app
app.run()
