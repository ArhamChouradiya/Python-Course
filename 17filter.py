#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:10:10 2019

@author: arham
"""

lst=[10,2,33,45,89,2]

result = list(filter(lambda x:x%2==0,lst))
print(result)