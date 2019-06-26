# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:29:38 2019

@author: Lenovo
"""

import pandas as pd
url = "http://www.panphol.com/data/page/stockprice/TOP#"
data = pd.read_html(url)
print(data[0])