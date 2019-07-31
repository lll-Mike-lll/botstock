# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 16:03:17 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['copy']

b = {2}
coll.insert_one(b)

