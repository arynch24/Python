#interview question

#this is not a comment 
#comments are completely ignored by the python interpreter
#docstring is used to document our code

def square(n):               #docstring must be just in next line of func def. otherwise it would not considered as a docstring.
    '''Takes in a number n,returns the             
    square of n''' 
    print(n**2)                          
square(5)
print(square.__doc__) #access docstring