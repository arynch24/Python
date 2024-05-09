class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(2*self.data)
        
node=Node(10)
print(node)
print(node.data)

class DLL:#keeps the addrss of node
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def size(self):
        return self.__size
    
    def is_empty(self):
        if(self.__size):
            return False
        else:
            return True
    
    def append(self,data):
        new_node=Node(data)
        if(self.is_empty()):
            self.__head=new_node
            self.__tail=new_node
        else:
            self.__tail.next=new_node
            new_node.prev=self.__tail
            self.__tail=new_node
        self.__size+=1
        
    def __str__ (self):
        l=[]
        trav=self.__head
        while(trav!=None):
            l.append(str(trav.data))
            trav=trav.next
        #return '<--->'.join(map(str,l))
        return "<--->".join(l)
    
    def add_first(self,data):
        new_node=Node(data)
        if(self.is_empty()):
            self.__head=new_node
        else:
            new_node.next=self.__head
            self.__head.prev=new_node
            self.__head=new_node
        self.__size+=1
    
    def add_at(self,index,data):
        if(0<=index and self.size()):
            raise Exception("Invalid Index")
        elif(index==0):
            self.add_first(data)
        elif(index==ll.size()-1):
            self.append(data)
        else:
            id=0
            trav=self.__head
            while id!=index-1:
                id+=1
                trav=trav.next
            
            new_node=Node(data,trav,trav.next)
            
            trav.next=new_node
            new_node.next.prev=new_node
        self.__size==1
    
    def remove_first(self):
        if(self.is_empty()):
            raise Exception("Invalid Index")
        else:
            temp=self.__head
            self.__head=
            
                    
            
    
ll=DLL()

ll.append(2)
ll.append(5)
ll.append(34)

ll.add_first(120)
ll.add_first(45957)
ll.add_first(1)

print(ll)
print(ll.size())