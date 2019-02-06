#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:02:06 2019

@author: hienh
"""
import json
import requests
import sqlite3

from flask import Flask,render_template,request
from searchdb import *
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='home')



@app.route("/business_search.html")
def business_search():
    return render_template("business_search.html", title = "search a business" )


@app.route("/business_result", methods=["POST"])
def business_result():
    form_data = request.form
    postcode = form_data["postcode"].upper().replace(' ','')

    if postcode:
        geolocation= display50Business(postcode)
        return render_template("business_result.html", title = "result", **locals())
    else:
        message = "need postcode"
        return render_template("index.html", title = "business result", **locals())

@app.route("/person_search.html")
def person_search():
    return render_template("person_search.html", title="search a person")

@app.route("/person_result", methods=["POST"])
def person_result():
    form_data = request.form
    name = form_data["name"]
    if name:
        return render_template("person_result.html", title="person result", **locals())
    else:
        message = "No matches found. Sorry!"
        print (message)
        return message


if __name__ == '__main__':
    app.run(debug =True)
