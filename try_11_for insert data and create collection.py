# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:21:07 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']

for i in range(6):
    coll = db['list'+str(i)]
    data = {'no':i+10}
    coll.insert_one(data)