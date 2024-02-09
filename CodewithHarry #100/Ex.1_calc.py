a=int(input("a:"))
b=int(input("b:"))
o=input("operation:")

def calc(a,b):
    if o=='+':
        print(a+b)
    elif o=='-':
        print(a-b)
    elif o=='*':
        print(a*b)
    elif o=='/':
        print(a/b)
    else: 
        print("operation is incorrect") 

calc(a,b)