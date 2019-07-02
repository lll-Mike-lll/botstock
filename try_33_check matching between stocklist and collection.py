# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:06:47 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock2']
coll = db.list_collection_names()

stock_name1 = []
for x in coll:
    stock_name1.append(x)

#print(stock_name1)

db2 = cli['stock']
coll2 = db2['stock_list']
get_name = coll2.find()

stock_name2 = []
for y in get_name:
    stock_name2.append(y['stock_name'])
    
#print(stock_name2)
print(type(stock_name1[0]))
print(type(stock_name2[0]))

for i in range(len(stock_name2)):
    k=0
    k2=0
    for j in range(len(stock_name1)):
        if stock_name1[j]==stock_name2[i]:
            k=k+1
        else:
            k2=k2+1
    if k==1:
        print(stock_name2[i] + ' update')
    elif k2==len(stock_name1):
        print(stock_name2[i] + ' //////////////// add')

for i in range(len(stock_name1)):
    k=0
    k2=0
    for j in range(len(stock_name2)):
        if stock_name1[i]==stock_name2[j]:
            k=k+1
        else:
            k2=k2+1
    if k2==len(stock_name2):
        print(stock_name2[i] + '')
   
    
        
        
            