a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
b=[[3,4,7],[4,4,3],[-2,3,6],[4,6,3]]
m=3
n=3
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(m):
    for j in range(n):
        for p in range(n):
            c[i][j]+=a[i][p]*b[p][i]

print(c)