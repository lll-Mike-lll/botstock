# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:50:39 2019

@author: Lenovo
"""




import pymongo as pm
cli = pm.MongoClient()
db = cli['stock2']
coll = db['unorder_date']
     
data2 = coll.find()
name = []
for n in data2:
    name.append(n['date'])    
print(name)

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
                    
print(name)


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
