with open("zoop.txt","r") as file:
    line=file.readline()
    
    while line:
        print(line,end="")
        line=file.readline()