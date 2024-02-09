#newList = [ iterator for iterator in existingList if (condition over iterator) in existingList ]

l = [12, 5, 4, 2, 11, 16, 23, 230, -9, 2, 1]

lMod = [i for i in l if i>5 in l]
print(lMod)

for i in range(0, len(l)):
    print(l[i])