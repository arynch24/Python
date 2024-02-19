
m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
i,j=0
n=4
circle=0
count=0
while(circle<n/2):
    cycle=n-1-2*circle
    jumps=0
    while(jumps<cycle):
        temp=m[i][i+jumps]
        m[i][j+jumps]=m[i+cycle-jumps][j]#bottom left to bottom right
        m[i+cycle-jumps][j]=m[i+cycle][j+cycle-jumps]
        m[i+cycle][j+cycle-jumps]



