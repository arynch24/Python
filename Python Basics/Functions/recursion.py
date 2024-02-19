#base condition
#logic
#recursion call
a=[1,2,3]
def printlist(a,i):
    #base condition-for break
    if(i>=len(a)): 
        return
    #logic
    print(a[i])
    #recursion
    printlist(a,i+1)
printlist(a,0)