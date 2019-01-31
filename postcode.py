#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:14:28 2019

@author: hienh
"""

import math

def distance(lat1,long1,lat2,long2):

    R = 6373.0 # approximate radius of earth in km

    dlon = radians(long2) - radians(long1)
    dlat = radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c