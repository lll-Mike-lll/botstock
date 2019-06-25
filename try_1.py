# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
url = "http://www.panphol.com/data/page/stockprice/TOP#"
data = pd.read_html(url)
print(data[0])

#print(data[0].iloc[0,1])
