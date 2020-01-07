#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 02:15:36 2019

@author: arham
"""

dict={1:"John",2:"Bob",3:"Bill"}
#print(dict)
#print(dict.items())

k=dict.keys()

for i in k:     #access keys
    print(i)
    
v=dict.values()
for i in v:     #access values
    print(i)
    
#print(dict[3])
    
del dict[2]     #delete element



