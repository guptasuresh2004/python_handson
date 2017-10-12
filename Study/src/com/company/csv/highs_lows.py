'''
Created on Oct 12, 2017

@author: Sku293
'''
import csv
filename = 'SampleCSVFile_119kb.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    #print(next(reader))
    
for index, column_header in enumerate(header_row):
        print(index, column_header)

data=[]
uni_data=[]
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[2]);
print()
print(len(data))

for dat in data:
    if dat not in uni_data:
        uni_data.append(dat)
    
print(uni_data)   
print(len(uni_data)) 
    
    