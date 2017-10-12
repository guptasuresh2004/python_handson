'''
Created on Oct 5, 2017

@author: Sku293
'''
#read entire file
try:
    with open('pi_digit11s.txt') as file_object:
        contents = file_object.read()
        print(contents.lstrip())
except Exception:
    print("unable to find file")
    
 #read file line by line   
with open('pi_digits.txt') as file_object:
    list_of_file= file_object.readlines()
    for temm in file_object:
        print(temm.strip())

#print(list_of_file.size())
print(list_of_file)
pi=""
for file_line in list_of_file:
    pi=pi+file_line.strip();
print(pi)    
print(pi[0:6].replace("3.14","suresh"))
print(pi)

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")