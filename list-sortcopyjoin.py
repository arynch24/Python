list = [100, 50, 65, 82, 23]
list.sort()
print(list)

list = [100, 50, 65, 82, 23]
list.sort(reverse=True)
print(list)

#Case sensitive sorting can give an unexpected result:
lsit1 = ["banana", "Orange", "Kiwi", "cherry"]
lsit1.sort()
print(lsit1)


#Perform a case-insensitive sort of the list:
list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort(key = str.lower)
print(list1)

list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.reverse()
print(list1)

list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

