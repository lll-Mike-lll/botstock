# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:00:44 2019

@author: Lenovo
"""
#import pandas as pd
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

data2 = coll.find()
name = []
for n in data2:
    name.append(n['stock_name'])
    
for i in range(100):
    print(name[i])


# =============================================================================
# data = coll.find_one()
# print(type(data))
# print(data)
# =============================================================================



# =============================================================================
# for k in range(1):
#     web_name = 'http://www.panphol.com/data/page/stockprice/'+name[k]
#     print(web_name)
#     data = pd.read_html(web_name)
#     db2 = cli['stock2']
#     coll2 = db2[name[k]]
#     print('c')
#     for i in range(len(data[0])):
#         data1 = {'date':data[0].iloc[i,0],
#              'open':data[0].iloc[i,1],
#              'max':data[0].iloc[i,2],
#              'min':data[0].iloc[i,3],
#              'close':data[0].iloc[i,4],
#              'change':data[0].iloc[i,5],
#              'percent chg':data[0].iloc[i,6],
#              'volume':int(data[0].iloc[i,7]),
#              'value':int(data[0].iloc[i,8])}
#         coll.insert_one(data1)
#     print('d')
# =============================================================================
