# flask_app.py
from flask import Flask
from flask import jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
	return "f u"
@app.route("/api")
def outputdata():
	data = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
	return data.to_json()
