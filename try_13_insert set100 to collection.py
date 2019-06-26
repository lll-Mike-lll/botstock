# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:43:49 2019

@author: Lenovo
"""

import pandas as pd
url = "https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH"
data1 = pd.read_html(url)
#print(data[2])
#print(type(data1[2].iloc[1,0]))

# =============================================================================
# for i in range(99):
#     print(data1[2].iloc[i,0])
# =============================================================================
    
import pymongo as pm
cli = pm.MongoClient()
db = cli['stock']

for i in range(99):
    coll = db['stock_list']
    data = {'stock_name':data1[2].iloc[i,0]}
    coll.insert_one(data)
