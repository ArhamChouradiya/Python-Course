#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:01:24 2019

@author: arham
"""

lst=[10,20,30,30.5]
lst.append(40)
lst.remove(20)
del(lst[1])
#lst.clear()
lst.insert(2,99)
lst1= lst.sort(reverse=True)
print(lst)

