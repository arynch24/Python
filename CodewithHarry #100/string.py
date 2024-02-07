
text = 'Hello'
text = "Hello"
print(text)
text = '''\nI am Aryan Chauhan
and I like python\n'''  # in the triple quote marks we can write multiline string
print(text)

str = "Vishwa Sir is our teacher"

# printing 'our' from the str
print(str[7: 10])

# printing alternate characters of string
print(str[: :2])

str = "My Dear Student"
print(str[-9: :-1 ])

# reversing the string
print(str[: :-1])

firstName = input("Enter your first name:")
lastName = input("Enter your second name:")

print("Your full name is:",firstName+" "+lastName)