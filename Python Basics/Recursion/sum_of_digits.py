def sum_digits(n):
    if(n==0):
        return 0 
    
    digit=n%10
    n=n//10
    return (digit+sum_digits(n))

n=123
print(sum_digits(n))
    