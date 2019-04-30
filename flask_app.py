# flask_app.py
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np
from flask import request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

i=1
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    __tablename__ = "CUSTOM_TABLE_NAME"
    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def hello():
	
	api_request = User(id=i, username="bob", email="bob@gmail.com")
	db.session.add(api_request)
	db.session.commit()
	return "f u"

@app.route("/api", methods=["GET","POST"])
def outputdata():
    if request.method == "GET":
        return str(jsonify(data))
	

    data = request.get_json(force=True)
    print(data)
    return jsonify(data)


   
    #You will need to adapt your app routing to `@app.route("/api", methods=["POST"])`
    #POSTed JSON is available from request.form (treat it like a dictionary).
    #Test on your local server, anything you print will be visible in the logs.
    #When you're ready, deploy and test against your production server.



