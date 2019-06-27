# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:38:59 2019

@author: Lenovo
"""

# =============================================================================
# import pymongo as pm
# cli = pm.MongoClient()
# 
# db = cli['stock']
# coll = db['aav']
# x = coll.find_one()
# print(x)
# 
# 
# db2 = cli['stock2']
# coll2 = db2['m']
# x2 = coll2.find_one()
# print(x2)
# =============================================================================

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

data2 = coll.find()
name = []
for n in data2:
    name.append(n['stock_name'])
    
db2 = cli['stock2']
coll2 = db2['stock_list']

for i in range(100):
    data = {'stock_name':name[i]}
    coll2.insert_one(data)

# =============================================================================
# for i in range(100):
#     print(name[i])
# =============================================================================

