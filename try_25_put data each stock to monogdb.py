# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:55:34 2019

@author: Lenovo
"""
import pandas as pd
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

data2 = coll.find()
name = []
for n in data2:
    name.append(n['stock_name'])

print('a')

db2 = cli['stock3']

for j in range(2):
    web_name = 'http://www.panphol.com/data/page/stockprice/'+name[j]
    data = pd.read_html(web_name)
    print('e')
    for i1 in range(len(data[0])):
        coll2 = db2[name[j]]
        i=len(data[0])-1-i1
        data1 = {'date':data[0].iloc[i,0],
             'open':data[0].iloc[i,1],
             'max':data[0].iloc[i,2],
             'min':data[0].iloc[i,3],
             'close':data[0].iloc[i,4],
             'change':data[0].iloc[i,5],
             'percent chg':data[0].iloc[i,6],
             'volume':int(data[0].iloc[i,7]),
             'value':int(data[0].iloc[i,8])}
        coll2.insert_one(data1)       
    print('b')    
print('c')

# =============================================================================
# for i in range(100):
#     data = {'stock_name':name[i]}
#     coll2 = db2['stock_list']
#     coll2.insert_one(data)
# =============================================================================
