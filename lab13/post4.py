# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 20:36:35 2025

@author: JENIL
"""

def merge_files(file1_path, file2_path, output_path):
    """
    Merges the contents of two text files into a third file.
    Contents of file1 come first.

    Args:
    file1_path (str): Path to the first file.
    file2_path (str): Path to the second file.
    output_path (str): Path to the output merged file.
    """
    try:
        with open(file1_path, 'r') as file1:
            content1 = file1.read()
        
        with open(file2_path, 'r') as file2:
            content2 = file2.read()
        
        with open(output_path, 'w') as output_file:
            output_file.write(content1)
            output_file.write(content2)
        
        print(f"Files merged successfully into {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    merge_files('file.txt', 'ict1.txt', 'merged.txt')
