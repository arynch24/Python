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
        ll=[]
        trav=self.__head
        while(trav!=None):
            ll.append(str(trav.data))
            trav=trav.next
        #return '<--->'.join(map(str,ll))
        return "<--->".join(ll)
    
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
    
    def removeFirst(self):
     
        if self.is_empty() :
            raise Exception('Empty List')
        
        self.__head =  self.__head.next
        self.__size -= 1

        if self.is_empty() :
            self.__tail = None
        else :
            self.__head.prev = None

    def removeLast(self):
    
        if self.is_empty() :
            raise Exception('Empty List')
    
        self.__tail = self.__tail.prev
        self.__size -= 1

        if self.is_empty() :
            self.__head = None
        else :
            self.__tail.next = None

    def __remove__(self, node):
        if node.prev == None :
            self.removeFirst()
            return
        
        if node.next == None :
            self.removeLast()
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        self.__size -= 1
        return None


    def removeAt(self, index):
        if index < 0 or index >= self.__size :
            raise Exception("Invalid index")
        
        trav = self.__head
        i = 0
        while i != index :
            trav = trav.next
        i += 1

        return self.__remove__(trav)



    def indexOf(self, data):
        trav = self.__head
        index = 0

        while trav is not None :
            if trav.data == data :
                return index
        
        index += 1
        trav = trav.next

        return -1


    def contains(self, data):
        return self.indexOf(data) != -1


    def clear(self) :
        pass

    def __iter__(self): 
        self.__iter = self.__head
        return self


    def __next__(self): 
        if self.__iter is None :
            raise StopIteration
        
        data = self.__iter.data
        self.__iter = self.__iter.next
        return data


    def __str__(self):
        ll = []
        trav = self.__head
        while trav is not None:
            ll.append(trav.data)
        trav = trav.next
        return '<->'.join(map(str, ll))


#Test the code
node = Node(5, None, None)
ll = DLL()
print(node.data)
print(len(ll))
print(ll.size())
print(ll.is_empty())
ll.append(5)
print(ll.size())
ll.removeLast(10)
print(ll)
ll.removeFirst(6)
print(ll)
ll.add_at(1, 15)
print(ll)
ll.removeAt(2)
print(ll)
print(ll.indexOf(10))
print(ll.contains(15))
print(ll.contains(19))