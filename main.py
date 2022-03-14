# import "packages" from flask
from flask import Flask, render_template,request
import requests
import json
import random
import math


# create a Flask instance
from __init__ import app

if __name__ == "__main__":
    app.run(debug=True, port="5002")