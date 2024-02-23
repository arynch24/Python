a=[]
for i in range(1,101):
    a.append(0)
i=1
while(i<101):
    for j in range(i,100,i):
        if(a[j]==0):
            a[j]=1
        elif(a[j]==1):
            a[j]=0
    i+=1
print(a)
count_o =0
count_c=0
for i in range(100):
    if (a[i]==1):
        count_o+=1 
    elif(a[i]==0):
        count_c+=1
print("open doors:",count_o)
print("close doors:",count_c)

