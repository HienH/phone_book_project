#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:24:09 2019

@author: hienh
"""

import json
import requests
import sqlite3


with open('md.js') as f:
    businessdata = json.load(f)
    
with open('people.js') as f:
    peopledata = json.load(f)


conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

   
def getpostcode():
    code = []
    for item in businessdata:
        code.append(item['postcode'])
    
    for people in peopledata:
        code.append(people['postcode'])
    
    code = list(set(code))
    return code

def getrequest():
    loadpostcode = getpostcode()
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    lon =[]
    lat =[]

    for i in loadpostcode:

        postcode_url= endpoint_postcode+ i
        post_response= requests.get(postcode_url).json()
        
        if post_response['status'] == 200:
            lon.append(post_response['result']['longitude'])
            lat.append(post_response['result']['latitude'])
            
        else:
            lon.append('NA')
            lat.append('NA')

        
    return [lon,lat]


#def create_table():
#    c.execute('CREATE TABLE IF NOT EXISTS postcodes1(postcode VARCHAR(15),longitude VARCHAR(15), latitude VARCHAR(15))')
#
#create_table() 

lonlag = getrequest()
post= getpostcode()

def data_entry():
       postcode= post[i]
       longitude = lonlag[0][i]
       latitude= lonlag[1][i]
       c.execute('INSERT INTO postcodes1( postcode,longitude,latitude ) VALUES(?,?,?)', ( postcode,longitude,latitude)) 
       conn.commit()

for i in range (len(post)):
    data_entry()
c.close()
conn.close()
