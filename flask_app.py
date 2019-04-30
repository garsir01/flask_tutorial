# flask_app.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "f u"
@app.route("/api")
def outputdata():




    jsonify(data)
