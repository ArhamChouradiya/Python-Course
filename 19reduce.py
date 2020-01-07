#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:14:47 2019

@author: arham
"""
from functools import reduce

lst =[5,10,15,20]

result = reduce(lambda x,y:x+y,lst)
print(result)

