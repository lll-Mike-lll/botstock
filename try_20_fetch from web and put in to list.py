# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:50:32 2019

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
#print(data[0].iloc[0,2])

#colume = ['date','open','max','min','close','change','percent chg','vloume','value']
#print(colume[0])
# =============================================================================
# for i in range(9):
#     print(colume[i])
# =============================================================================

# =============================================================================
# n1 = []
# data_row = data[0].shape[1]
# for i in range(data_row):
#     n1.append(data[0].iloc[0,i])
# =============================================================================

# =============================================================================
# m = data[0].iloc[0,7]
# m2 = int(data[0].iloc[0,7])
# print(m)
# print(m2)
# print(type(m))
# print(type(m2))
# #print(data[0])
# =============================================================================

# =============================================================================
# for j in n1:
#     print(j)
# =============================================================================
    
for i in range(len(data[0])):
    data1 = {'date':data[0].iloc[i,0],'open':data[0].iloc[i,1],'max':data[0].iloc[i,2],'min':data[0].iloc[i,3],'close':data[0].iloc[i,4],'change':data[0].iloc[i,5],'percent chg':data[0].iloc[i,6],'volume':int(data[0].iloc[i,7]),'value':int(data[0].iloc[i,8])}
    coll.insert_one(data1)

# =============================================================================
# for i in range(9):
#     print(data[0].iloc[0,i])
#     print(i)
# =============================================================================
    
for i in range(len(data[0])):
    data1 = {'date':data[0].iloc[i,0],'open':data[0].iloc[i,1],'max':data[0].iloc[i,2],'min':data[0].iloc[i,3],'close':data[0].iloc[i,4],'change':data[0].iloc[i,5],'percent chg':data[0].iloc[i,6],'volume':int(data[0].iloc[i,7]),'value':int(data[0].iloc[i,8])}
    coll.insert_one(data1)