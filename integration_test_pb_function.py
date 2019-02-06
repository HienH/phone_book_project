#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:44:33 2019

@author: hienh
"""

from searchdb import *


class TestSearch():
    
    
    
#    def getBusinessDB(self): 
#        self.getDb = self.getDb()
#        return self.getDb
##    
    def test_get_user_postcode(self):
        self.postcode = get_user_postcode()
        return self.postcode
        
    def test_getuser_geolocation(self):
        self.geolocation = getuser_geolocation("SE8 4AS")
        if self.geolocation:
            return True
        else:
            print("Cannot find geolocation with given postcode")
            return False 
  
    def filterPostcodes(self):        
        self.filterPostcodes= filterPostcodes()
        if self.filterPostcodes:
            return "top 50"
        else:
            return False
            
    def run_tests(self):
#        print(self.getBusinessDB())
        print(self.test_get_user_postcode())
        print(self.test_getuser_geolocation())
        print(self.filterPostcodes())

    
if __name__ == "__main__":
    newTest = TestSearch()
    newTest.run_tests()    