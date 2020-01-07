#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:17:19 2019

@author: arham
"""

class flight:
    def __init__(self,engine):
        self.engine=engine
    def starteng(self):
        self.engine.start()
        
class airbusengine:
    def start(self):
        print("Starting airbus engine")
        
class boingengine:
    def start(self):
        print("Starting boing engine")
        
ae=airbusengine()
f=flight(ae)
f.starteng()
be=boingengine()
f1=flight(be)
f1.starteng()