# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:47:19 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list3']

data = coll.find()
f_data = []
for i in data:
#    print(i['stock_name'])
    f_data.append(i['stock_name'])

#print(type(data))
print(f_data)
print(len(f_data))
print(type(f_data[1]))

db2 = cli['stock']
coll2 = db2['copy_stock_list2']

for i in range(len(f_data)):
    m = {'stock_name':f_data[i]}
    coll2.insert_one(m)

data2 = coll2.find()
f_data2 = []
for i in data2:
    f_data2.append(i['stock_name'])

n = 0
for j in range(len(f_data2)):
    for k in range(len(f_data)):
        if f_data2[j]==f_data[k]:
            n=n+1

if n==len(f_data2):
    print('complete')
    
#    print(f_data[i])




