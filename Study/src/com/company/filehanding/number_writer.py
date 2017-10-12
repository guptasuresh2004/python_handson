'''
Created on Oct 5, 2017

@author: Sku293
'''
import json

numbers = [2, 3, 5, 7, 11, 13,"suresh"]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)