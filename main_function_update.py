# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:32:25 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock2']
coll = db.list_collection_names()

stock_list = []
for i in coll:
    stock_list.append(i)
print(stock_list)
print(len(stock_list))

for i11 in range(1):
    loop_db1 = []
    coll2 = db[stock_list[i11]]
    data2 = coll2.find()
    for n in data2:
        loop_db1.append([n['date'],
                 n['open'],
                 n['max'],
                 n['min'],
                 n['close'],
                 n['change'],
                 n['percent chg'],
                 n['volume'],
                 n['value']])
    
print(loop_db1[0][0])
