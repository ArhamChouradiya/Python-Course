#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:33:54 2019

@author: arham
"""

class duck:
    def talk(self):
        print("QUACK QUACK")
        
class human:
    def talk(self):
        print("HELLO")
        
def calltalk(obj):
    obj.talk()
    
d=duck()
calltalk(d)
h=human()
calltalk(h)