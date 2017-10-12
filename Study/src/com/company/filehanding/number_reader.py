'''
Created on Oct 5, 2017

@author: Sku293
'''
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
lenth=len(numbers)
print(lenth)