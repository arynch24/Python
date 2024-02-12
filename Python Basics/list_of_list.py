m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
row=4
col=4
i=0
j=0
count=1
while row >=0 and col>=0:
    jump=0
    while(jump<col):
        m [i][j]=count
        j+=1
        jump+=1
        count+=1
    row-=1
    i+=1
    j+=1

print(m)