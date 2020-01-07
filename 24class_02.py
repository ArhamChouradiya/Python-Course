#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 12:48:21 2019

@author: arham
"""



"""PARAMETERISED CONSTRUCTOR""" 
class Course:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
        
    def average(self):
        num=len(self.rating)
        average=sum(self.rating)/num
        print(average)
        
        
c1=Course("arham",[1,2,3,4,5])

print(c1.name)
print(c1.rating)
c1.average()