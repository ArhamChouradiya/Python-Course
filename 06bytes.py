#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 02:07:50 2019

@author: arham
"""

lst=[20,30,40]
b=bytes(lst)
"""donot support item assignment
b[4]=30
"""
print((b))

b1=bytearray(lst)
#print(b1)
b1[2]=33
print(b1)