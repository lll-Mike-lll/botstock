# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:02:33 2019

@author: Lenovo
"""

import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']

coll = db['stock_list']
data = {'stock_name':"work"}
coll.insert_one(data)