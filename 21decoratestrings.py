#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:54:37 2019

@author: arham
"""

def decor(fun):
    def inner(n):
        return fun(n)+". How are you?"
    return inner


@decor
def hello(name):
    return "Hello "+name

print(hello("Arham"))