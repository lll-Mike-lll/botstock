# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:50:34 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()


db2 = cli['xx']
data2 = db2.list_collection_names()
print('a')
print(data2)