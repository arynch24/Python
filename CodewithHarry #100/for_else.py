name="Aryan Chauhan"
for i in name:
    print(i)
else:
    print("I came out of the loop")


list = [222,3,32,23,32,2,11,3,1,3,537,47,4,74,7,7,7,4,4]

for i in list:
    print(i,end="-")
    if (i==7):
        break
else:
    print("This statemnet will not execute")
