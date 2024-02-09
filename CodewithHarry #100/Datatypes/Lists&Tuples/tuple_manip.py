t1 = (12, 34, "IITG", 50, 92, 123, 987, -98, "PWIOI" )

# let we have to change the 4th index element to some text and PWIOI to some complex number

# convert t1 to list

t1 = list(t1)

t1[4] = -23.324
t1[len(t1)-1] = complex(-12, 23)
print(type(t1))

# change back to tuple

t1 = tuple(t1)
print(type(t1))

print(t1)