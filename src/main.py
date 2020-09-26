#!/usr/bin/python3.8

import flask
import sqlalchemy
import pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1> Hello World! </h1>"

@app.route('/login', methods=['GET'])
def login(req, res):
	username = req.username
	password = req.password

	#hash the password

	#ask mysql if this combo exists

	#return token if correct
	#false if not

	return res

app.run()
