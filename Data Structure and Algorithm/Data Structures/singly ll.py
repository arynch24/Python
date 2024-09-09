class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList:
    def __init__(self):
        self.__size=0
        self.head=None
        self.tail=None

    # Check whether Linked list is empty or not 
    def is_empty(self):
        return self.__size==0                   
    
    # To get the size an linked list
    def size(self):
        return self.__size


    # To Append an element
    def append(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:                                       
            trav=self.head
            while trav.next:                       
                trav=trav.next
            trav.next=newNode                      

        self.__size +=1                             

    # Adding element to 0th Position
    def add_First(self,data):
        newnode=Node(data)
        if self.size()==0:                        
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head              
            self.head.next=self.head.next.next
            self.head=newnode
            
        self.__size+=1


    # Adding element to (n-1)th Position
    def last_element_addition(self,data):
        newNode=Node(data)
        if(self.size()==0):
            self.head=newNode
            self.tail=newNode
        else:                               
            trav=self.head
            while(trav.next):
                trav=trav.next
            trav.next=newNode
            newNode.next=None
        
        self.__size+=1

    # Adding element to a given index Position
    def add_index(self,index,data):
        if(index < 0 or index > self.size()):              
            raise Exception ("Index is not present... ")
        if index==0:                            
            self.add_First(data)                            
        elif index==self.size():
            self.append(data)                               
        else:
            trav=self.head              
            for _ in range(index - 1):                      
                trav = trav.next
            newnode = Node(data, trav.next)
            trav.next = newnode                            
            self.__size += 1


    # Deleting first element from the linked list
    def remove_First(self):                 
        if self.is_empty():
            raise Exception ("Removing Impossible : List is empty")
        self.head=self.head.next                          
        
        self.__size-=1


    # Deleting last element from the linked list
    def remove_last(self):
        if self.is_empty():
            raise Exception ("Removing Impossible : List is empty")
        if self.size()==1:
            self.head=None             
        else:
            prev = None
            trav = self.head
            while trav.next:
                prev = trav
                trav = trav.next
            prev.next = None
        self.__size -= 1

    # # Deleting ith index element from the linked list
    def remove_index(self,index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of range...")           
        if index == 0:
            self.remove_first()                              
        else:
            trav = self.head                                
            for _ in range(index - 1):
                trav = trav.next
            trav.next = trav.next.next
            self.__size -= 1

    # Reversing a linked list
    def reverse(self):
        prev = None
        trav = self.head
        while trav:
            next_node = trav.next
            trav.next = prev
            prev = trav
            trav = next_node
        self.head = prev

    # Merging linked lists

    def merge_list(self,newl):
        if self.is_empty():
            self.head=newl.head
        else:
            trav=self.head                                     
            while trav.next:
                trav=trav.next                                
            trav.next=newl.head
        self.__size += newl.__size

    # Middle of list

    def middle_list(self):
        if self.is_empty():
            raise Exception ("Linked List is emtpy .... ")
        s=self.head                              
        f=self.head                              
        while f and f.next:
            s=s.next                              
            f=f.next.next                         

        return s.data
        
     # printing elements of liked list   
    def print_linked_list(self):
        trav = self.head
        while trav:
            print(trav.data, end=' ')
            trav = trav.next
        print()


ll=SinglyLinkedList()

# Sol. 1:

ll.append(67)
ll.append(176)
ll.append(153)
ll.append(206)
ll.print_linked_list()
print(ll.size()) # size of list
print()
# Sol. 2:

ll.remove_index(2)
ll.print_linked_list()
print(ll.size())
print()

# Sol. 3:

print("Size of linked list :",ll.size())
print()

# Sol. 4:

print(ll.is_empty())
print()





# Sol. 6:

ll.reverse()
ll.print_linked_list()
print()

# Sol. 7:

ll.last_element_addition(15)
ll.last_element_addition(25)
ll.print_linked_list()
print()

# Sol. 8:

ll.add_First(30)
ll.add_First(35)
ll.print_linked_list()
print()


# Sol. 9:

# To merge we have to first make linked list . So, let's make:
l2=SinglyLinkedList()
l2.append(40)
l2.append(45)
l2.append(50)
ll.merge_list(l2)
print("Required Merged list :")
ll.print_linked_list()
print("Length of merged list :",ll.size())
print()



# Sol. 11:

print("Middle Element of Liked List :",ll.middle_list())
print()