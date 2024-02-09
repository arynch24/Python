# function to calculate fatorial of a number

def factorial(n):
    if(n == 1 or n == 0):   # base condition
        return 1
    else:
        return n*factorial(n-1)   # recursive statement

# calling function

a = int(input("Enter number:"))
print(factorial(a))

# let's calculate fibonacci series upto n-terms

def fibonacci(a, b, n):
    if n == 0:
        return     # base condition
    else:
        print(a+b," ")   # printing from third term
        fibonacci(b, a+b, n-1)   # function call with new term and decreasing n


a = 0
b = 1
n = int(input("Enter the number of terms:"))
print(a,"\n",b)
fibonacci(a, b, n-2)