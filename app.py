#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:02:06 2019

@author: hienh
"""
import json
import requests
import sqlite3

from flask import Flask,render_template
from searchdb import * 
app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    
    businesses = getherdatabaseInfo_select()

    search= request.form.get('searchBusiness')
#    search = search.lower().title()
#    category_list = []
#    for key, values in businesses.items():
#        if search_catergory in values:
#            category_list.append(key)
#    if category_list == [] :
#        print("none found")
#    else:
#        print(category_list)
#    
   


    return render_template("index.html", title = "home")

    c.close()
    conn.close() 

  

if __name__ == '__main__':
    app.run(debug =True)
      
