#When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


##for cahnginhg anything in tuple just like adding or removing convert it into list first thna in tuple.