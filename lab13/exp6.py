# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 10:15:27 2025

@author: JENIL
"""
with open(r"C:\Users\JENIL\Desktop\python\ict.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

