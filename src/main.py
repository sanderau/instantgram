#!/usr/bin/python3.8

import flask
import werkzeug
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

# connect to mysql
cnx = mysql.connector.connect(**config)

## Helper Functions ##

def user_exists(username):
	cursor = cnx.cursor()

	query = "SELECT * FROM users WHERE username = '{}'".format(username)

	cursor.execute(query)
	r = cursor.fetchone()

	cursor.close()

	if r == None:
		return False # The user does not exist, so return false.
	else:
		return True # The user does exist, so return true

def insert_user(username, email, password):
	cursor = cnx.cursor()

	query = "INSERT INTO users (username, email, password) VALUES ('{}', '{}', '{}')".format(username, email, password)
	cursor.execute(query)

	cursor.close()

	return None

## Error Handlers ##

@app.errorhandler(400)
def missing_data(e):
	return flask.jsonify(error=str(e)), 400

@app.errorhandler(409)
def user_already_exists(e):
	return flask.jsonify(error=str(e)), 409

## App Routes ##

@app.route('/signup', methods=['PUT'])
def sign_up():
	# get the json data from the request
	json_data = flask.request.json

	#check to see if they sent all the correct data
	if ( "username" not in json_data ) or ( "password" not in json_data ) or ( "email" not in json_data ):
		flask.abort(400, description="Did not include all fields")

	# get the username, password, and email from the request
	username = json_data["username"]
	password = json_data["password"]
	email = json_data["email"]

	# see if the user exists
	if( user_exists(username) ):
		flask.abort(409, description="User already exists")
	else:
		insert_user(username, email, password)
		resp = flask.jsonify(success=True)
		return resp
		
		

@app.route('/', methods=['GET'])
def home():
	return "<h1> Hello World! </h1>"

# run app
app.run()
