#concatenation in python

def rec(name,marks):
    print(name+" "+marks)

rec("aryan", "98")

#arbitary arguments
def list(*fruit):
    print("My fav fruit is:"+fruit[2])

list("kela","angur","aaam")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#list as argument

def func(food):
   for x in food:
      print(x)

fruit=["kela","angur","aaam"]
func(fruit)