r=int (input("row:"))
c=int (input("column:"))
m=[]
for i in range(r):
    m.append([])

print(m)

for i in range(r):
    for j in range(c):
        x=int(input(f"Enter number for row:{i} & column:{j} ="))
        m[i][j].append(x)

# m=[[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1]]
count =0
max_row=[0,0,0,0,0]
for i in range(len(m)):
    for j in range(len(m)):
        if(m[i][j]==1):
            count+=1
    max_row[i]=count
    count=0
#maxx is maximum value in max row
maxx=max(max_row)
#max -row is array of count 1.
#here we are finding index of maximum count value in aar max_row
ans=max_row.index(maxx)
print(ans)


