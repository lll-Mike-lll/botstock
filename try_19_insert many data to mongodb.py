# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:29:56 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
name = 'aav'
coll = db[name]

data1 = {'date':'2',
         'min':'12'}

coll.insert_one(data1)
