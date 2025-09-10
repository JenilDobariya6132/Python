# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 20:24:19 2025

@author: JENIL
"""
def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count lines: split by newline and count
        lines = len(content.split('\n'))
        
        # Count words: split by whitespace and count
        words = len(content.split())
        
        # Count characters: total length of content
        characters = len(content)
        
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {characters}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the filename
count_file_stats('file.txt')

