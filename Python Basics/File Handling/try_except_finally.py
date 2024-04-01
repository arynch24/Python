try:
    file =open("zoop.txt","r")
except FileNotFoundError:
    print("File not found")
    
except PermissionError:
    print("Permisssion Denied")

finally:
    file.close()    