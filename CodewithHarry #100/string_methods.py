str = "Python is easy language"

# upper and lower

print(str.upper(), "and", str.lower())

str = "   NLP  "

# strip

print(str.strip())   # will remove space from both sides
print(str.lstrip())  # will remove space from left side
print(str.rstrip())  # will remove space from right side

# rstrip

str = "Hello!!!!!"

print(str.rstrip("!"))

# replace

str = "Hello!!!!! Hello!!!"

print(str.replace("Hello", "Hii"))

# split

str = "Hello how are you"
list1 = str.split(" ")
print(list1)

# capitalize

str = 'This wiLl convErt the first leTter to upPercase and reSt all of theM with lowrCase'

print(str.capitalize())

# centre

str = "HII"
print(str.center(50))
print(len(str.center(50)))
print(str.center(23, '.'))

# count

str = "We have to build something new"
print(str.count('e'))

# endswith

print(str.endswith('w'), str.endswith('e'))

# find()

print(str.find('to'))
print(str.find('hii'))

# isalnum and islpha

str = "Hood007"
print(str.isalnum())
str = "alphabet"
print(str.isalpha())
str = "apjo2344"
print(str.isalpha())

# islower

str = 'sfdsf'
print(str.islower())

# isprintable

str = " fsf\t and \n"
print(str.isprintable())

# title

str = "We have to build something new"
print(str.title())

# swapcase

print(str.swapcase())