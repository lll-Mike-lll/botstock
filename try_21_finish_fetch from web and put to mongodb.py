# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:57:21 2019

@author: Lenovo
"""

name = 'aav'

web_name = 'http://www.panphol.com/data/page/stockprice/'+name
print(web_name)
print('a')

import pandas as pd
data = pd.read_html(web_name)

print('b')

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db[name]

print('c')

for i in range(len(data[0])):
    data1 = {'date':data[0].iloc[i,0],
             'open':data[0].iloc[i,1],
             'max':data[0].iloc[i,2],
             'min':data[0].iloc[i,3],
             'close':data[0].iloc[i,4],
             'change':data[0].iloc[i,5],
             'percent chg':data[0].iloc[i,6],
             'volume':int(data[0].iloc[i,7]),
             'value':int(data[0].iloc[i,8])}
    coll.insert_one(data1)
    
print('d')