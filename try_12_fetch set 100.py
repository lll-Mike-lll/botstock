# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:30:42 2019

@author: Lenovo
"""
import pandas as pd
url = "https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET100&language=th&country=TH"
data = pd.read_html(url)
#print(data[2])

for i in range(100):
    print(data[2].iloc[i,0])

