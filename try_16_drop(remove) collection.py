# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:36:33 2019

@author: Lenovo
"""
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']
coll = db['test_1']
coll.drop()
