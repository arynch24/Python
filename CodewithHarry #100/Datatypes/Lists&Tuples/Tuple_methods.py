

t = (1, 2, 45, 45, 66, 66, 77, 45, 3, 2, 2, 1)

# count
#tupleName.count(element)
print(t.count(2))
print(t.count(45))
print(t.count(66))
print(t.count(1))

# Index
#tuple.index(element, start, end)
print(t.index(45)) # it detects first occurence
print(t.index(45, 3, 4))
print(t.index(66, 5, 6))