#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:56:34 2019

@author: arham
"""

a,b=10,5
#print(a,b,sep='')
'''sep used to define seperator in print. default is space'''
#print("a is %i, b is %.2f"%(a,b))
#print("a is {}, b is {}".format(a,b))
#print("a is {0}, b is {1}".format(a,b))

"""Input
s=input("Enter name:")
print(s)
"""
"""INteger input
i=int(input("Enter integer"))
print(i)
"""

lst=[int(x) for x in input().split(' ')] #split by anything
print(lst)
