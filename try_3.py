# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:59:54 2019

@author: Lenovo
"""

import pandas as pd
url = "http://www.panphol.com/data/page/stockprice/TOP#"
data = pd.read_html(url)
print(data[0].index.size)
print(data[0].columns.size)
print(type(data[0]))
#print(data)
print(data[0].iloc[[0,1]])
print(data[0].iloc[[0,2]])
print(data[0].iloc[[2,3,4]])
print(data[0].iloc[0,2])
