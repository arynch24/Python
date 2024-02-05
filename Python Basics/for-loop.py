l = [2,45,78,12,12,12,12,"pwioi" , 6+7j,[56,67,78,"dsfdsf"]]
#q1 . try to print index of all the element 
#q2 . Try to extract all the list of char if element is string 
#q3 . Try to return a list after doing a square of all the int element 

for i in range(len(l)):
    print("index" , i  , "for an element " , l[i])
print("_________")
for i in range(5,len(l),2):
    print("index" , i  , "for an element " , l[i])
#range(start,stop,update or jump)