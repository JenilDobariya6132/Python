
import csv
# Reading from a CSV file
with open(r'C:\Users\JENIL\Desktop\python\data.csv', 'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
