# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:41:15 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
print(db.list_collection_names())

