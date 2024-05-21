class Node:
    def __init__ (self,data =None, next=None):
        self.data=data
        self.next = next
        
class stack:
    def __init__(self):
        return self.sz
    
    def size(self) :
        return self.size()==0
    
    def push(self,element):
        newNode=Node(element,head)
        self.head =newNode
        self.sz+=1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("stack Underflow")
        temp=self.head 
        data =temp.data
        self.head=self.head.next
        del temp 
        return data
    
    def top(self):   
        if self.isEmpty():
            raise Exception("stack Underflow")
        return self.head.data