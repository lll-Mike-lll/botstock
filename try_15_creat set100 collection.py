# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:07:47 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll1 = db['stock_list']
data = coll1.find()
j=0
name_1 = []
for i in data:
    name_1.append(i['stock_name'])
    j=j+1

print(len(name_1))


    
#for i in range(10):
    
# =============================================================================
# for i in data:
#     coll = db[i['stock_list']]
# =============================================================================
    