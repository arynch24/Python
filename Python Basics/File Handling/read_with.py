#define the file path
file_path="zoop.txt"


#by using with statement we need not to worry about closing the file.
with open(file_path,"r") as file:
    
    #read the content of the file
    file_contents=file.read()
    
    #process the file contents
    print("File contents:")
    print(file_contents)
    
    #type of file pointer
    print("Type of the file pointer:",type(file))
    
    #print the file pointer itself
    print("File pointer:",file)