i =0
j=0
n=5
for i in range(5):
    for j in range(5):
        if j<=i or j>=n-i-1 :
            print("*",end=" " )
        else:
            print(end="  ")
        
    print()