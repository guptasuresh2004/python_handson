'''
Created on Oct 5, 2017

@author: Sku293
'''
print("enter two number to get devison of these")
print("enter q to quit!")
while True:
    f_n=input("Please enter first number")
    s_n=input("Please enter second number")
    if f_n=="q" or s_n=="q":
        break
    else:
        try:
            d=int(f_n)/int(s_n)
            print(d)
        except Exception:
            print("you can not devide by zero")
        
        
        