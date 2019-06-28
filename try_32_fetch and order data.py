# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:54:28 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock2']
coll = db['AAV']
     
data2 = coll.find()
name = []
name2 = []
name3 = []
name4 = []
for n in data2:
    name.append(n['date'])
    name3.append([n['date'],
                 n['open'],
                 n['max'],
                 n['min'],
                 n['close'],
                 n['change'],
                 n['percent chg'],
                 n['volume'],
                 n['value']])
#print(name)
#print(name3)
    
    
print(name[0][0:2])
print(name[0][3:5])
print(name[0][6:10])

a = int(name[0][0:2])
print(a-20)

#lately to older
for j in range(0,len(name)-1):
    for i in range(0,len(name)-1):
        a1 = int(name[i][0:2])
        a2 = int(name[i][3:5])
        a3 = int(name[i][6:10])
        b1 = int(name[i+1][0:2])
        b2 = int(name[i+1][3:5])
        b3 = int(name[i+1][6:10])
        if a3<b3:
            move = name[i]
            name[i] = name[i+1]
            name[i+1] = move
        elif a3==b3:
            if a2<b2:
                move = name[i]
                name[i] = name[i+1]
                name[i+1] = move
            elif a2==b2:
                if a1<b1:
                    move = name[i]
                    name[i] = name[i+1]
                    name[i+1] = move

#print(name)

#insert ordered data to list
kk=0
for i1 in range(10):
    for j1 in range(len(name3)):
        kk=kk+1
#        if name[i1]==name3[j1][0]:
#            name2.append(name3[j1])

print(len(name3))
#print(len(name))
#print(len(name3))
#print(name3[0])
#print(name2)   
#print(len(name2))

# =============================================================================
# db55 = cli['stock4']
# coll55 = db55['AAV']
# #table1 = ['date','open','max','min','close','change','percent chg','volume','value']
# for i in range(len(name2)):
#     data1 = {'date':name2[i][0],
#              'open':name2[i][1],
#              'max':name2[i][2],
#              'min':name2[i][3],
#              'close':name2[i][4],
#              'change':name2[i][5],
#              'percent chg':name2[i][6],
#              'volume':int(name2[i][7]),
#              'value':int(name2[i][8])}
#     coll55.insert_one(data1)       
# =============================================================================
