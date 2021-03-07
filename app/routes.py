#!/usr/bin/env python3
# -*- coding utf8 -*-
"""Route Definitions"""


from flask import Flask
app = Flask(__name__)
from about_me.app import app

@app.route("/")
def index():
    return "hello, world!"


@app.route("/about")
def about():
    deandre = {
        "first_name": "DeAndre",
        "last_name": "Fuentes",
        "what I like to do": "politics"
    }
    return deandre






# @app.route("/user")
# def scan_user():
#     out = get_all_users()
#     return out