#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:28:21 2019

@author: arham
"""

class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    class engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("engine started")
            
c =car("BMW",2017)
e=c.engine(123)
e.start()