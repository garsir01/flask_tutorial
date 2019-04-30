# flask_app.py
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
from flask import request


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
	return "f u"
@app.route("/api", methods=["POST"])
def outputdata():
	data = {'me':'you'}
	data = request.get_json(force=True)
	print(data)	
	return jsonify(data)


   
    #You will need to adapt your app routing to `@app.route("/api", methods=["POST"])`
    #POSTed JSON is available from request.form (treat it like a dictionary).
    #Test on your local server, anything you print will be visible in the logs.
    #When you're ready, deploy and test against your production server.



