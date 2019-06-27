# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:14:18 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

data = coll.find()
name = []
for n in data:
    name.append(n['stock_name'])
    
    
for i in range(100):
    print(name[i])

# =============================================================================
# l1 = []
# j=1
# for i in range(10):
#     l1.append([i,j])
# 
# for k in range(10):    
#     print(l1[k][1])
# =============================================================================
