with open("output.txt","w") as file:
    file.write("Hello, World ! \n")
    file.write("This is a new line.")
    
with open("output.txt","r") as file_read:
    content=file_read.read()
    print(content)
    
new_lines=["Addittional line 1\n","Additiional line 2\n"]
with open("output.txt","a") as file:
    file.writelines(new_lines)


with open("output.txt","r") as file_read:
    content=file_read.read()
    print(content) 