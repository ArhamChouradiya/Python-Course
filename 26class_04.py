#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:15:19 2019

@author: arham
"""

class student:
    major= "CSE"
    
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        
s1=student(1,"JOhn")
s2=student(2,"jane")
print(s1.major)
print(student.major)