#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:56:48 2019

@author: hienh
"""

import json
import requests
import sqlite3

def getDb():
    try:
        conn = sqlite3.connect('phonebook.db')
        cursor = conn.cursor()
        return cursor
    except:
        return False
getDb()

#
#conn = sqlite3.connect('phonebook.db')
#c = conn.cursor()

#
#
#def getherdatabaseInfo_select():
##      getDb()
#
#      c.execute(""" SELECT
#                            businessphonebook.id,
#                            businessphonebook.business_name,
#                            businessphonebook.city,
#                            businessphonebook.country,
#                            businessphonebook.postcode,
#
#                            postcodes1.longitude,
#                            postcodes1.latitude,
#
#                            businessphonebook.tel,
#                            businessphonebook.business_category
#
#
#                            FROM businessphonebook
#
#                            INNER JOIN postcodes1 ON (businessphonebook.postcode = postcodes1.postcode)
#
#                            """)
#
#
#      b_infoDict = {}
#
#      for b_id, b_name,  city, country, postcode, lat, lon, tel, cat in c.fetchall():
#          b_infoDict[b_id] = b_id, b_name,  city, country, postcode, lat, lon, tel, cat
#      return b_infoDict


def getBusiness():
    getDb()

    try:
        business = input("What category? ")
        business = business.lower().title()
        c=getDb()
        c.execute(" SELECT * FROM businessphonebook WHERE business_category = ?",(business,))
        business = c.fetchall()
        if business == [] :
            print("Please enter correct Category ")
        else:
             print(business)
             return business

    except ValueError:
        print("Enter appropriate Category ")

getBusiness()

#businesses = getherdatabaseInfo_select()
##print(businesses)

#def getBusinessCategory():
#
#    search_category = search_category.lower().title()
#    category_list = []
#    for key, values in businesses.items():
#        if search_catergory in values:
#            category_list.append(key)
#    if category_list == [] :
#        print("none found")
#    else:
#        print(category_list)




#getBusinessCatefory()

#for name, age in businesses.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
#    if age == search_age:
#        print(name)
##wordFind = input("Enter word: ")   # raw_input for Python2, input for Python3
##wordFind = wordFind.lower().capitalize()
##find_first = wordFind[0]
##matches = businesses[find_first]
##print(matches)
#
#
#def getBusinessbyType():
#      c.execute(""" SELECT * businessphonebook.business_category   """)
#
#      for row in c.fetchall():
#          print(row)



#def getBusiness(location=None, category=None):
#
#    db = getdb()
#
#
#
#    if category:
#        query2 = "SQL for all businesses where category = ?"
#    elif location:
#        query3 = "sql for all busineeses where location = ?"
#
#    elif location and category:
#        query4 "sql for all businesses where location = ? and type = "
#    else:
#        query1 = "SQL FOR All businesses"
#
