# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 20:28:24 2025

@author: JENIL
"""

def read_file_lines(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        print("Lines in the file:")
        for line in lines:
            print(repr(line))  # To show newlines
        print("\nFull list:")
        print(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_file_lines('file.txt')
