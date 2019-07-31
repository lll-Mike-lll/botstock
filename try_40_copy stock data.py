# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:21:12 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list3']

data = coll.find()
data_name = []
for i in data:
#    print(i['stock_name'])
    data_name.append(i['stock_name'])


#get collection name for mongodb
db2 = cli['stock6']
data2 = db2.list_collection_names()
print('a')
print(data2)
print(len(data2))
print(type(data2[0]))
print('a')

db3 = cli['xx']
m = data2[1]
coll2 =db2[m]
data3 = coll2.find()
zzdata = []
for n in data3:
    zzdata.append({'date':n['date'],
                      'open':n['open'],
                      'max':n['max'],
                      'min':n['min'],
                      'close':n['close'],
                      'change':n['change'],
                      'percent chg':n['percent chg'],
                      'volume':n['volume'],
                      'value':n['value']})
print(zzdata)
#for j in range(len(zzdata)):
#    data_set_mike = {'date':zzdata[i][0],
#                      'open':zzdata[i][1],
#                      'max':zzdata[i][2],
#                      'min':zzdata[i][3],
#                      'close':zzdata[i][4],
#                      'change':zzdata[i][5],
#                      'percent chg':zzdata[i][6],
#                      'volume':zzdata[i][7],
#                      'value':zzdata[i][8]}
#print(data_set_mike)
print(len(zzdata))
coll3 = db3[data2[1]]
coll3.insert_many(zzdata)
#print(zzdata)
print(m)
    
    
# =============================================================================
# db3 = cli['copy_stock_1']
# for i in range(len(data2)):
#     m = data2[i]
#     coll2 =db2[m]
#     data3 = coll2.find()
#     zzdata = []
#     for n in data3:
#         zzdata.append([n['date'],
#                   n['open'],
#                   n['max'],
#                   n['min'],
#                   n['close'],
#                   n['change'],
#                   n['percent chg'],
#                   n['volume'],
#                   n['value']])
#     data_set_mike = []
#     for j in range(len(zzdata[i])):
#         data_set_mike = {'date':zzdata[0],
#                          'open':zzdata[1],
#                          'max':zzdata[2],
#                          'min':zzdata[3],
#                          'close':zzdata[4],
#                          'change':zzdata[5],
#                          'percent chg':zzdata[6],
#                          'volume':zzdata[7],
#                          'value':zzdata[8]}
#     coll3 = db3[data2[i]]
#     coll3.insert_one(data_set_mike)
#     print(m)
# =============================================================================

# =============================================================================
# #get data from each collection
# coll2 =db2[data2[0]]
# data3 = coll2.find()
# zzdata = []
# for n in data3:
#      zzdata.append([n['date'],
#                   n['open'],
#                   n['max'],
#                   n['min'],
#                   n['close'],
#                   n['change'],
#                   n['percent chg'],
#                   n['volume'],
#                   n['value']])
# #print(data4)
# =============================================================================

