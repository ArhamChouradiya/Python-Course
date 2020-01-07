#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:25:10 2019

@author: arham
"""

class student:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    def setnm(self,nm):
        self.name=nm
    def getnm(self):
        return self.name
    
s=student()
s.setid(123)
s.setnm("Jack")
print(s.getid(),s.getnm())