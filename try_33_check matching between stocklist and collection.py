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

update_list = []
add_list = []
insert_list = []

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
        update_list.append(stock_name2[i])
    elif k2==len(stock_name1):
        print(stock_name2[i] + ' //////////////// add')
        add_list.append(stock_name2[i])

for i in range(len(stock_name1)):
    k=0
    k2=0
    for j in range(len(stock_name2)):
        if stock_name1[i]==stock_name2[j]:
            k=k+1
        else:
            k2=k2+1
    if k2==len(stock_name2):
        print(stock_name1[i] + ' ////////////////insert')
        insert_list.append(stock_name1[i])

import pandas as pd

for i2 in range(len(add_list)):
    print(add_list[i2])

kk = 0

#update data in list of add_list
# =============================================================================
# for j22 in range(len(add_list)):
#     print(add_list[j22])
#     web_name22 = 'http://www.panphol.com/data/page/stockprice/'+add_list[j22]
#     data22 = pd.read_html(web_name22)
#     print('e')
#     for i1 in range(len(data22[0])):
#         coll22 = db[add_list[j22]]
#         #reverse order older to recently
#         i=len(data22[0])-1-i1
#         data122 = {'date':data22[0].iloc[i,0],
#              'open':data22[0].iloc[i,1],
#              'max':data22[0].iloc[i,2],
#              'min':data22[0].iloc[i,3],
#              'close':data22[0].iloc[i,4],
#              'change':data22[0].iloc[i,5],
#              'percent chg':data22[0].iloc[i,6],
#              'volume':int(data22[0].iloc[i,7]),
#              'value':int(data22[0].iloc[i,8])}
#         coll22.insert_one(data122)
#     kk=kk+1
#     print('b')
#     print(kk/len(add_list)*100)
# =============================================================================

# =============================================================================
# for i1 in range(len(update_list)):
#     data3 = []
#     name_i1 = update_list[i1]
#     print(name_i1)
#     print(i1)
#     web_name = 'http://www.panphol.com/data/page/stockprice/' + name_i1
#     print('aa')
#     print(web_name)
#     data = pd.read_html(web_name)
#     print('a')
#     coll3 = db[name_i1]
#     print('b')
#     data2 = coll3.find()
#     print('c')
#     for n in data2:
# #        print(n)
#         data3.append([n['date'],
#                  n['open'],
#                  n['max'],
#                  n['min'],
#                  n['close'],
#                  n['change'],
#                  n['percent chg'],
#                  n['volume'],
#                  n['value']])
# #    print(data3)
#     k2=0
#     for i in range(len(data[0])):
#         k=0
#         for j in range(len(data3)):
#             if data[0].iloc[i,0]==data3[j][0]:
#                 k=1
#                 k2=k2+1
#                 break  
#         if k==0:
#             print('add')
#             print(data[0].iloc[i,0])
#             data1 = {'date':data[0].iloc[i,0],
#                  'open':data[0].iloc[i,1],
#                  'max':data[0].iloc[i,2],
#                  'min':data[0].iloc[i,3],
#                  'close':data[0].iloc[i,4],
#                  'change':data[0].iloc[i,5],
#                  'percent chg':data[0].iloc[i,6],
#                  'volume':int(data[0].iloc[i,7]),
#                  'value':int(data[0].iloc[i,8])}
#             coll3.insert_one(data1)       
#         if k2==len(data[0])-1:
#             print('they are updated')
# =============================================================================
    
# =============================================================================
# print(update_list)
# print(len(update_list))
# print(add_list)
# print(len(add_list))
# print(insert_list)
# print(len(insert_list))
# =============================================================================
        
        
            