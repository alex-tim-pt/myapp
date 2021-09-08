
import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def hello_world():
    """The default controller function"""
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

