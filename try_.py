# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:18:40 2019

@author: Lenovo
"""
file = open("mike.txt","w")
for x in range(6):
    file.write("hello2")
file.write("line2")
file.write("line2")
file.write("line2")
file.close()