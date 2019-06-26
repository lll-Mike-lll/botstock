# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:02:33 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['stock_list']

#add name in this
#add name in this
#add name in this
name_add = 'top'
#add name in this
#add name in this
#add name in this

name_list = coll.find()
a = []
i=0

for x in name_list:
    a.append(x['stock_name'])
j=0    
for y in range(len(a)):
    name_a = a[y]    
    if name_add.upper() == name_a.upper():
        print('there is one at '+ str(y))
        j=1

if j==0:
    data = {'stock_name':name_add.upper()}
    coll.insert_one(data)
    print('add finished')
else:
    print('does not insert')

# =============================================================================
# x1 = 'mike'
# x2 = "mike"
# print(type(x1))
# print(type(x2))
# =============================================================================

