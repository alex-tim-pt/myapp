
import datetime

from flask import Flask
from flask import render_template

from models import Employee


app = Flask(__name__)



@app.route("/")
def hello_world():
    """The default controller function"""
    return "<p>Hello, My World!</p>"

@app.route("/employees")
def show_emploeeys():
    """The default controller function"""
    emps = Employee.select()

    return render_template(
        'employees.html',
        employees=emps
    )

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


