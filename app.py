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



@app.route("/business_search", )
def business_search():
    return render_template("business_search.html", title = "search")


@app.route("/business_results",methods=["POST"])
def business_results():
    form_data = request.form
    name = form_data["business_name"]
    if name:
        busines_names = find_business_by_name(name)
        if (isinstance(busines_names,list)):
            return render_template("business_results.html", title = "businessresults", **locals())
        else:
            message_name = "No such name in directory"
            return render_template("business_search.html", title = "search", **locals())

@app.route("/businesscategory_results",methods=["POST"])
def business_cat():
    form_data = request.form
    category = form_data["category"]
    if category:
        busines_category = business_by_category(category)
        if (isinstance(busines_category,list)):
            return render_template("businesscategory_results.html", title = "businesscategoryresults", **locals())
        else:
            message_category = "No such category in directory"
            return render_template("business_search.html", title = "search", **locals())


@app.route("/business_postcode_result",methods=["POST"])
def business_by_postcode():
    form_data = request.form
    postcode = form_data["postcode"]
    if postcode:
        business_postcode = filterPostcodes(postcode)
        if (isinstance(business_postcode,list)):
            return render_template("business_postcode_results.html", title = "businesspostcoderesults", **locals())
        else:
            message_postcode = "Incorrect postcode"
            return render_template("business_search.html", title = "search", **locals())

@app.route("/person_search.html")
def person_search():
    results = get_people()
    people_list = []
    for result in results:
        people_list.append(result)
    return render_template("person_search.html", title="search a person", people=people_list)

# @app.route("/person_result", methods=["POST"])
# def person_result():
#     form_data = request.form
#     name = form_data["name"]
#     people = find_person_by_name(name)
#     if name:
#         return render_template("person_result.html", title="person result", people=people)
#     else:
#         message = "No matches found. Sorry!"
#         return message


if __name__ == '__main__':
    app.run(debug =True)
