# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:59:04 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
col = db['stock_list']

da1 = col.find()
name_stock = []
for n in da1:
    name_stock.append([n['_id'],n['stock_name']])
    
#print(name_stock)

# =============================================================================
# for i in range (len(name_stock)):
#     print(i)
# =============================================================================
x = 0
for i in range (len(name_stock)):
    for j in range (len(name_stock)):
        if name_stock[i][1]==name_stock[j][1]:
            print(name_stock[i][1])
            x=x+1
        
print(x)
    
#print(name_stock[0][0])
#col.delete_one({'_id':name_stock[1][0]})

print(len(name_stock))

