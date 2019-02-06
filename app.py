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
def home():
        
    return render_template("index.html", title = "home" )



@app.route("/result", methods=["POST"])
def result():
    form_data = request.form
    postcode = form_data["postcode"].upper().replace(' ','')
    
    if postcode:
        geolocation= display50Business(postcode)
        return render_template("result.html", title = "result", **locals())
    else:
        message = "need postcode"
        return render_template("index.html", title = "result", **locals())
    
    

  
if __name__ == '__main__':
    app.run(debug =True)
      
