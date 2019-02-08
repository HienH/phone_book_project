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


def get_user_postcode():
   user_postcode = input('Please enter your postcode:').upper().replace(' ','')
   if len(user_postcode) <=9:
       return user_postcode
   else:
       return False

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
    user_post = user_post.upper().replace(' ','')
    database = getBusinessDB()
    try: 
        user_log_lat = list(getuser_geolocation(user_post))
        busi = {}
        for row in database:
           business_lat_lat= list(row[6:8])
           dist = distance(user_log_lat[0],user_log_lat[1],float(business_lat_lat[0]),float(business_lat_lat[1]))
           busi[row[1]]= dist
        sorted_by_distance = sorted(busi.items(), key=lambda kv: kv[1])
        top50byDistance = sorted_by_distance[:50]

        return top50byDistance
    except:
        print("incorrect postcode")
        
def getBusiness_top50(user_post):
    top50 = filterPostcodes(user_post)
    database = getBusinessDB()
    category_list = []
    if category_list !=[]:
        for value in top50 :
            for row in database:
                if value[0] == row[1]:
                    category_list.append(row)
        return category_list
    else:
        return ("sorry please enter correct postcode ")
  

       
    


def find_business_by_name(name):
    results = getBusinessDB()
    business_name_list = []
    for row in results:
        business_name = row[1]
        if name.capitalize() in business_name:
           business_name_list.append(row)

    if business_name_list==[]:
        return "cannot find name"

    else:
        return business_name_list
    


def business_by_category(category):
    results = getBusinessDB()
    business_list = []
    for row in results:
        businesscategory = row[9]
        if category.lower() in businesscategory.lower() :
            business_list.append(row)

    if business_list==[]:
        return "cannot find" +category+ " shop near you"

    else:
        return business_list


bname = input("search for a business name: ")
print(find_business_by_name(bname))

buisness_name = input("what business category are you looking for? ")
print(business_by_category(buisness_name))

post = input("please enter your postcode ")
print(getBusiness_top50(post))


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


