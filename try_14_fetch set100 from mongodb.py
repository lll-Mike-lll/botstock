# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:53:48 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

data = coll.find()
for i in data:
    print(i['stock_name'])

