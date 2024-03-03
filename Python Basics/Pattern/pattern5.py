n=7
for i in range(n):
  for j in range(n):
    if(j==i or i+j == n-1):
     if i+j == (n-1):
        print('/', end = '')
     else:
        print('\\', end = '')
    else:
        print('*', end = '')
  print()