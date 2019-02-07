#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:15:02 2019

@author: hienh
"""

import json
import requests
import sqlite3
from math import sin, cos, sqrt, atan2, radians


def getDb():
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        print('hello')
        return cursor
    except:
        return False

#Making sure SQL queries are running appropriately
def query_db():
    db = getDb()
    try:
        test_query = "SELECT * FROM business_table"
        db.execute(test_query)
    except:
        return None

#######################SEARCH BUSINESS ######################################

def getBusinessDB():
      db= getDb()
      query = db.execute(""" SELECT
                            businessphonebook.id,
                            businessphonebook.business_name,
                            businessphonebook.address,
                            businessphonebook.city,
                            businessphonebook.country,
                            businessphonebook.postcode,

                            postcodes1.longitude,
                            postcodes1.latitude,

                            businessphonebook.tel,
                            businessphonebook.business_category


                            FROM businessphonebook

                            INNER JOIN postcodes1 ON (businessphonebook.postcode = postcodes1.postcode)

                            """)
      results = query.fetchall()
      return results

#######################GE USER POSTCODE ######################################


#def get_user_postcode():
#    user_postcode = input('Please enter your postcode:').upper().replace(' ','')
#    if len(user_postcode) <=9:
#        return user_postcode
#    else:
#        return False

def getuser_geolocation(user_post):
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    postcode_url= endpoint_postcode+user_post
    post_response= requests.get(postcode_url).json()
    if post_response['status'] == 200:
            lon = post_response['result']['longitude']
            lat =post_response['result']['latitude']
            return lon,lat
    else:
        print("Please enter correct postcode")
        return False

def distance(lat1,long1,lat2,long2):
    R = 6373.0 # approximate radius of earth in km
    dlon = radians(long2) - radians(long1)
    dlat = radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist

def filterPostcodes(user_post):
    database = getBusinessDB()
    user_log_lat = list(getuser_geolocation(user_post))
    busi = {}
    for row in database:
       business_lat_lat= list(row[5:7])
       dist = distance(user_log_lat[0],user_log_lat[1],float(business_lat_lat[0]),float(business_lat_lat[1]))
       busi[row[1]]= dist
    sorted_by_distance = sorted(busi.items(), key=lambda kv: kv[1])
    top50 = sorted_by_distance[:51]
    return top50


def find_business_by_name(name): 
    results = getBusinessDB() 
    error = "cannot find name"
    business_name_list = []
    for row in results:
        business_name = row[1]
        if name.capitalize() in business_name:
           business_name_list.append(row)
    
    if business_name_list==[]:
        return error
    
    else:
        return business_name_list

print(find_business_by_name('Dynabox'))

def display50Business(user_post):
    try:
        category_list = []
        top50 = filterPostcodes(user_post)
        database = getBusinessDB()
        for values in top50:
            for data in database:
                if values[0] == data[1]:
                    category_list.append(data)

        return category_list

    except Exception as e:
        print (e)


#- enter postcode/ category
#- find relevant and closest store


###############################################################################
### PEOPLE FUNCTIONS

def get_people():
    db = getDb()
    query = "SELECT DISTINCT * FROM peoplephonebook"
    db.execute(query)
    results = db.fetchall()
    return results

def find_person_by_name(name): #Passed tests
    results = get_people() #Gets first_name, last_name, postcode, telephone_number
    people_list = []
    for row in results:
        print (row)
        firstName = row[0]
        lastName = row[1]
        if name.lower() in firstName.lower() or name.lower() in lastName.lower():
            results_list.append(row)
    return people_list

def find_person_by_postcode(postcode): #Passed tests
    input_postcode = str(postcode).replace(' ','').strip().lower()
    results = get_people()
    people_by_postcode = []
    for row in results:
        db_postcode = row[3].replace(' ','').strip().lower() #Converting postcodes from table into lower case with stripped whitespace
        if input_postcode in db_postcode:
            people_by_postcode.append(row)
    final_list = sorted(people_by_postcode, key = lambda x: x[1][1], reverse = True)
    for person in final_list:
        print (person)
    return final_list
