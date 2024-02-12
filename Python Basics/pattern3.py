n=50
for i in range(50):
    for j in range(50):
        if j==i:
            print("\\",end="")
        elif i+j==n-1:
            print("/",end="")
        else:
            print("*",end=" ")
    print()