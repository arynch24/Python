b=[[1,2],[3,2],[1,3]]
a=[[1,2,3],[3,2,1]]
n=2
p=2
m=3
c=[[0,0],[0,0]]
for i in range (0,n):
    for j in range(0,p):
        c[i][j]=0
        for k in range(0,m):
            c[i][j]+=a[i][k]*b[k][j]
print(c)