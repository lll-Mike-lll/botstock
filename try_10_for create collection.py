# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:18:54 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()

m='4'
db = cli['stock'+m]
coll = db['m']
data = {'name':"n"}
coll.insert_one(data)