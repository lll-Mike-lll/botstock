# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:50:39 2019

@author: Lenovo
"""
name = 'AAV'
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock2']
coll = db[name]

data2 = coll.find()
name2 = []

for n in data2:
    name2.append([n['date'],
                 n['open'],
                 n['max'],
                 n['min'],
                 n['close'],
                 n['change'],
                 n['percent chg'],
                 n['volume'],
                 n['value']])

#print(name2)

web_name = 'http://www.panphol.com/data/page/stockprice/'+name
print(web_name)
print('a')
import pandas as pd
data = pd.read_html(web_name)
#print(data)
#print(len(data[0]))
#print(len(name2))
#print(name2[23][0])
#print(data[0].iloc[5,0])
#print(type(name2[23][0]))
#print(type(data[0].iloc[5,0]))
#print(name2)
k2=0
for i in range(len(data[0])):
    k=0
    for j in range(len(name2)):
        if data[0].iloc[i,0]==name2[j][0]:
            k=1
            k2=k2+1
            break
        
    if k==0:
        print('add')
        print(data[0].iloc[i,0])
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
    if k2==len(data[0])-1:
        print('they are updated')
        
# =============================================================================
# import pymongo as pm
# cli = pm.MongoClient()
# db = cli['stock2']
# coll = db['unorder_date']
#      
# data2 = coll.find()
# name = []
# for n in data2:
#     name.append(n['date'])    
# print(name)
# 
# print(name[0][0:2])
# print(name[0][3:5])
# print(name[0][6:10])
# 
# a = int(name[0][0:2])
# print(a-20)
# 
# #lately to older
# for j in range(0,len(name)-1):
#     for i in range(0,len(name)-1):
#         a1 = int(name[i][0:2])
#         a2 = int(name[i][3:5])
#         a3 = int(name[i][6:10])
#         b1 = int(name[i+1][0:2])
#         b2 = int(name[i+1][3:5])
#         b3 = int(name[i+1][6:10])
#         if a3<b3:
#             move = name[i]
#             name[i] = name[i+1]
#             name[i+1] = move
#         elif a3==b3:
#             if a2<b2:
#                 move = name[i]
#                 name[i] = name[i+1]
#                 name[i+1] = move
#             elif a2==b2:
#                 if a1<b1:
#                     move = name[i]
#                     name[i] = name[i+1]
#                     name[i+1] = move
# =============================================================================
                    
                    
# =============================================================================
# #older to lately
# for j in range(0,len(name)-1):
#     for i in range(0,len(name)-1):
#         a1 = int(name[i][0:2])
#         a2 = int(name[i][3:5])
#         a3 = int(name[i][6:10])
#         b1 = int(name[i+1][0:2])
#         b2 = int(name[i+1][3:5])
#         b3 = int(name[i+1][6:10])
#         if a3>b3:
#             move = name[i]
#             name[i] = name[i+1]
#             name[i+1] = move
#         elif a3==b3:
#             if a2>b2:
#                 move = name[i]
#                 name[i] = name[i+1]
#                 name[i+1] = move
#             elif a2==b2:
#                 if a1>b1:
#                     move = name[i]
#                     name[i] = name[i+1]
#                     name[i+1] = move
# =============================================================================
                    
#print(name)


# =============================================================================
# x=[1, 8, 2, 3, 4, 0, 6, 9, 7, 5]
# 
# import pymongo as pm
# cli = pm.MongoClient()
# db = cli['stock']
# coll = db['aav']
# 
# data2 = coll.find()
# name = []
# for n in data2:
#     name.append(n['date'])
# 
# #print(name)
# 
# db2 = cli['stock2']
# coll2 = db2['unorder_date']
# for i in x:
#     data = {'date':name[i]}
#     coll2.insert_one(data)
# 
# print('a')
# =============================================================================
    

# =============================================================================
# db2 = cli['stock2']
# coll2 = db2['stock_list']
# 
# for i in range(100):
#     data = {'stock_name':name[i]}
#     coll2.insert_one(data)
# =============================================================================
