# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:14:49 2019

@author: Lenovo
"""
x = [2,1,6,5,3,8,4,9,7,0]
y = []
#for i in range(len(x)):

# =============================================================================
# for j in range(0,len(x)-1):
#     if x[j]>x[j+1]:
#         move = x[j]
#         x[j] = x[j+1]
#         x[j+1] = move
#     y[j]=x[j]
#     print(y)
# =============================================================================
for i in range(0,len(x)-1):    
    for j in range(0,len(x)-1):
        if x[j]>x[j+1]:
             move = x[j]
             x[j] = x[j+1]
             x[j+1] = move
    print(x)
             
print(x)