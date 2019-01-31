#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:23:08 2019

@author: hienh
"""
import json
import random
import sqlite3


with open('people.js') as f:
    peopledata = json.load(f)
    
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS peoplephonebook(id REAL, name TEXT , lastname TEXT , address VARCHAR(255), city TEXT, country TEXT,postcode VARCHAR(10), tel REAL )')

create_table()

def data_entry():
        id = random.randrange(101, 200)
        name= people['first_name']
        lastname = people['last_name']
        address= people['address_line_1']
        city= people['address_line_2']
        country= people['address_line_3']
        postcode=people['postcode']
        tel = people['telephone_number']
        c.execute('INSERT INTO peoplephonebook(id, name,lastname, address, city, country,postcode, tel  ) VALUES(?,?,?,?,?,?,?,?)', (id, name,lastname, address, city, country,postcode, tel)) 
        conn.commit()
        
for people in peopledata:
    data_entry()
c.close()
conn.close()       