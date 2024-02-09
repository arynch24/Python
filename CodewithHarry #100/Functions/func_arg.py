#Default
def avg(a=9, b=10):
    print(f"Average of {a} and {b}",(a+b)/2)

avg()  # will take 9 and 10
avg(1, 4) # 1 and 4 will overwrite 9 and 10 
avg(3)  # here a will be 3 and b will be default i.e. 10

print("______________________________________________________")
#Keyword Argument
def subt(a, b):
    print(f"subtraction of {a} and {b}",a-b)

subt(a=10, b=1)
subt(b=17, a=14)
subt(b=10, a=35)
print("______________________________________________________")
#Required Arguments
def name(firstName, middleName, lastName):
    print("Hello,", firstName, middleName, lastName)

name("Aryan", "", "Chauhan")

