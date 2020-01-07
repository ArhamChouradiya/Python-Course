#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:43:22 2019

@author: arham
"""

"""ASSERT STATEMENT
x=int(input())
assert x>10, "WRONG"
print("You entered",x)
"""

def average(a=0,b=0):   #Default Argument
    print(a,b)
    
average(b=10,a=20)  #Keyword Argument
average(10,20)   
average(a=30)   