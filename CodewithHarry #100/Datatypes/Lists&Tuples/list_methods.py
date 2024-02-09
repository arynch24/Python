
list1 = [12, "Shoyeb", "Ansari", "Prakhar", 13, -83, 3.14]

# 1. appned
list1.append(2.7453)
print("Append\n",list1)

# 2. insert
list1.insert(4, "Aryan")
print("Insert\n",list1)

list2 = [5, 6, 7]

# 3. extend
list1.extend(list2)
print("Extend1\n",list1)
list2.extend(list1)
print("Extend2\n",list2)

# removal

# 4. remove
list2.remove(5) # returns none
print("Remove\n",list2)

# 5. pop
c = list1.pop()
print(f"{c} is removed from {list1}")

# any index
b = list1.pop(2)
print(f"{b} is removed from {list1}")

# 6. reverse
list1 = [12, 45, -12.34, "Kolkata"]
list1.reverse()
print("reverse\n",list1)

# 7. copy
list3 = list()
list3 = list1.copy()
print("copy\n",list3)

# 8. sorting
l1 = [1000, 1234, -9234, 98734, 12345456, 12, 12, 12, 12]
l1.sort()
print("sort\n",l1)

# 9. count
print("Count\n",l1.count(12))
