#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:22:58 2019

@author: arham
"""

class objectcounter:
    num = 0
    def __init__(self):
        objectcounter.num+=1
    @staticmethod                #I don't know why it is used
    def display():
        print(objectcounter.num)
        
        
a=objectcounter()
q=objectcounter()
s=objectcounter()
d=objectcounter()
objectcounter.display()       