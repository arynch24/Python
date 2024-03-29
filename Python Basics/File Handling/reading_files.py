file=open("zoop.txt","r")

#read entire content of the file
content_entire =file.read()
print(content_entire)

#read single line from the file as a string
content_single_line=file.readline()

#reads all lines from the file and return them as a list.
content_readlines=file.readlines()

#close the file
file.close()
