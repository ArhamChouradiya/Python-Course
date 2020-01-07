#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:02:58 2019

@author: arham
"""

def customgen(x,y):
    while(x<y):
        yield x
        x+=1
        
result=customgen(9,18)

for i in result:
    print(i)
