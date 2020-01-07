#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:49:20 2019

@author: arham
"""

import sys

lst=sys.argv

for i in lst:print(i)
print(len(lst))

print(lst[0])

print("Product is:", int(lst[1])*int(lst[2]))