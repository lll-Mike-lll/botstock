# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:50:46 2019

@author: Lenovo
"""

import pymongo as pm
a = pm.MongoClient()
db = a['mike1']
print(db.collection_names())