#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:17:48 2019

@author: arham
"""

x=3

def ave():
    x=2
    print(x)#local
    print(globals()['x'])#global
    
"""ave()  #invoking ave function """
z=ave
z()
z()
z()