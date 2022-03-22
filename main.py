# import "packages" from flask
from week0 import menus, treedraw
from week1 import fibonacci, listsandloops

# create a Flask instance
from __init__ import app

if __name__ == "__main__":
    app.run(debug=True, port="5002")