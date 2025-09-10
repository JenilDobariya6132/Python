# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 11:00:57 2025

@author: JENIL
"""

import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])
    file.close()
