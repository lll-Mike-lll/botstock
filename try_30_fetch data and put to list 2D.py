# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:09:23 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['aav']

data2 = coll.find()
name = []

# =============================================================================
# for i in data2:
#     print(i)
# =============================================================================
    
for n in data2:
    name.append([n['date'],
                 n['open'],
                 n['max'],
                 n['min'],
                 n['close'],
                 n['change'],
                 n['percent chg'],
                 n['volume'],
                 n['value']])
print(name) 
