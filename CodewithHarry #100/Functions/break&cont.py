# Exit the loop when user input odd number'
a = int(input("Enter the number:"))
while True:
    if(a % 2 !=0 ):
        break
    a = int(input("Enter the number:"))

#continue
n=int(input("Enter a number:"))
while (n<100):
    n=n+1
    if (n%2==0):
        print(f"{n} is even number")
        continue

   
