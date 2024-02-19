#python can have multiple datatypes
list1 = ["abc", 34, True, 40, "male"]

#1. append
list1.append("apple")
print(list1)

#2. insert() method inserts an item at the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#3. extend to add another list to the list
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)

