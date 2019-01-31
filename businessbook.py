#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:18:26 2019

@author: hienh
"""
import json
import random
import sqlite3


###########import data#############


from getpostcode import *


with open('md.js') as f:
    businessdata = json.load(f)
    


conn = sqlite3.connect('phonebook.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS businessphonebook(id REAL, business_name TEXT , address VARCHAR(255), city TEXT, country TEXT,postcode VARCHAR(10), tel REAL,business_category TEXT )')

create_table()

def data_entry():
        id = random.randrange(1, 100)
        business_name= data['business name']
        address= data['address_line_1']
        city= data['address_line_2']
        country= data['address_line_3']
        postcode=data['postcode']
        tel = data['telephone_number']
        business_category = data['business_category']
        c.execute('INSERT INTO businessphonebook(id, business_name, address, city, country,postcode, tel ,business_category ) VALUES(?,?,?,?,?,?,?,?)', (id, business_name, address, city, country,postcode, tel ,business_category)) 
        conn.commit()
        
        
def get_data():
    c.execute("SELECT * FROM businessphonebook WHERE ")
    
    result =  any(elem in list1  for elem in list2)

        
for data in businessdata:
    data_entry()
    
    
    
c.close()
conn.close()    

    

