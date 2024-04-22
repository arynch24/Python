
#hackerrank 
def sum_digit(n):
    if(n==0):
        return 0
    digit=n%10
    n=n//10
    return (digit+sum_digit(n))

def superDigit(n):
    if(n<10):
        return n
    n=sum_digit(n)
    return superDigit(n)

k=4
n=9875
s=str(n)*k
n=int(s)
print(superDigit(n))


