'''
Created on Oct 5, 2017

@author: Sku293
'''
import json
filename="username.json"
with open(filename) as o_user_data:
    name=json.load(o_user_data)
    print("Welcome back  "+name)