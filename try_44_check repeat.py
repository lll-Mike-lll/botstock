# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:21:37 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['copy_stock_list2']

data = coll.find()
d2 = []
for n in data:
    d2.append([n['_id'],n['stock_name']])

#print(d2[0][0])
#print(type(d2[0][0]))
print(d2[0])


d3 = []
m2 = 0
for i in range(len(d2)):
    m=0
    d4 = []
    for j in range(len(d2)):
        if i!=j:
#            print('j')
            if d2[i][1]==d2[j][1]:
                m=m+1
                d4.append(d2[i])
    if m!=0:
        d3.append(d4)
        m2 = m2+1
if m2==0:
    print('it is complete')
else:
    print(len(d3))
    print(d3)
    print(m)
    print(m2)