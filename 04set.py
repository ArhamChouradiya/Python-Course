#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:52:18 2019

@author: arham
"""

s={10,20,30,"XYZ",10,20}
#print(s)

s.update([88,99])
#print(s)

#no slicing,indexing,repetition

s.remove(10)
print(s)

"""FROZEN SET"""
f=frozenset(s)
print(f)