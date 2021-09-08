
import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
    """The default controller function"""
    return "<p>Hello, World!</p>"

