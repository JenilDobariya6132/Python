# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 20:35:59 2025

@author: JENIL
"""

import csv

def read_and_print_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

if __name__ == "__main__":
    read_and_print_csv('output.csv')
