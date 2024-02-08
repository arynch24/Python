str = "My name is Aryan Chauhan"

# i is iterator, it is starting from 0
for i in str:
    print(i,end="-")

print()    

colors = ["blue", "red", "Green", "violet", "Purple"]

for color in colors: # color is the variable which is iterating over list colors
    print(color)
    # we can also iterate over color, since it is string
    for char in color:
        print(char)


# printing number from 1 to 100
        
for k in range(1, 101):
    print(k,end=" ")

print()
# printing odd number between 1 to 50
    
for i in range(1, 51, 2):
    print(i, end=" ")