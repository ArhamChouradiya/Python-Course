#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:02:46 2019

@author: arham
"""

class programmer:
    def setname(self,n):
        self.name=n
    def getname(self):
        return self.name
    def setsal(self,sal):
        self.salary=sal
    def getsal(self):
        return self.salary
    def settech(self,tech):
        self.tech=tech
    def getech(self):
        return self.tech
    
p1=programmer()
p1.setname("JOHN")
p1.setsal(50000)
p1.settech("JAVA")
print(p1.getname())
print(p1.getsal())
print(p1.getech())