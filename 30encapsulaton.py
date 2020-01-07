#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:15:35 2019

@author: arham
"""

class student:
    def __init__(self):
        self.__id=123       #__ for making it private
        self.__name="JOHN"
    def display(self):
        print(self.__id,self.__name)
        
s=student()
#s.display()
print(s._student__id);   #it is not completely private
"""_classname__variablename will access private data.this is called
        NAME MANGLING   """