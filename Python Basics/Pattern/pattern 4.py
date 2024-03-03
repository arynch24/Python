n=7
for i in range(int(n/2)):
  for j in range(n):
    if j<=i or j>=n-i-1 :
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()

count = int(n/2)
while(count>=0):
    for j in range(n):
      if j<=count or j>=n-count-1 :
        print("*", end=" ")
      else :
        print(" ",end=" ")
    print()
    count -=1