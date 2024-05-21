#include <iostream>

class Node {
public:
    int data;
    Node* prev;
    Node* next;
    
    Node(int data, Node* prev = nullptr, Node* next = nullptr) : data(data), prev(prev), next(next) {}
};

class DoublyLinkedList {
private:
    int size;
    Node* head;
    Node* tail;
    
public:
    DoublyLinkedList() : size(0), head(nullptr), tail(nullptr) {}
    
    ~DoublyLinkedList() {
        clear();
    }
    
    int len() const {
        return size;
    }
    
    bool isEmpty() const {
        return size == 0;
    }
    
    void append(int data) {
        if (isEmpty()) {
            head = tail = new Node(data);
        } else {
            tail->next = new Node(data, tail, nullptr);
            tail = tail->next;
        }
        size++;
    }
    
    void addLast(int data) {
        append(data);
    }
    
    void addFirst(int data) {
        if (isEmpty()) {
            head = tail = new Node(data);
        } else {
            head->prev = new Node(data, nullptr, head);
            head = head->prev;
        }
        size++;
    }
    
    void addAt(int index, int data) {
        if (index < 0 || index > size) {
            throw std::out_of_range("Index out of range");
        }
        
        if (index == 0) {
            addFirst(data);
        } else if (index == size) {
            addLast(data);
        } else {
            Node* trav = head;
            for (int i = 0; i < index - 1; i++) {
                trav = trav->next;
            }
            Node* newNode = new Node(data, trav, trav->next);
            trav->next->prev = newNode;
            trav->next = newNode;
            size++;
        }
    }
    
    int peekFirst() const {
        if (isEmpty()) {
            throw std::logic_error("List is empty");
        }
        return head->data;
    }
    
    int peekLast() const {
        if (isEmpty()) {
            throw std::logic_error("List is empty");
        }
        return tail->data;
    }
    
    void removeFirst() {
        if (isEmpty()) {
            throw std::logic_error("List is empty");
        }
        Node* temp = head;
        head = head->next;
        if (head) {
            head->prev = nullptr;
        } else {
            tail = nullptr;
        }
        delete temp;
        size--;
    }
    
    void removeLast() {
        if (isEmpty()) {
            throw std::logic_error("List is empty");
        }
        Node* temp = tail;
        tail = tail->prev;
        if (tail) {
            tail->next = nullptr;
        } else {
            head = nullptr;
        }
        delete temp;
        size--;
    }
    
    void removeAt(int index) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of range");
        }
        if (index == 0) {
            removeFirst();
        } else if (index == size - 1) {
            removeLast();
        } else {
            Node* trav = head;
            for (int i = 0; i < index; i++) {
                trav = trav->next;
            }
            trav->prev->next = trav->next;
            trav->next->prev = trav->prev;
            delete trav;
            size--;
        }
    }
    
    int indexOf(int data) const {
        Node* trav = head;
        int index = 0;
        while (trav) {
            if (trav->data == data) {
                return index;
            }
            trav = trav->next;
            index++;
        }
        return -1;
    }
    
    bool contains(int data) const {
        return indexOf(data) != -1;
    }
    
    void clear() {
        while (!isEmpty()) {
            removeFirst();
        }
    }
    
    class Iterator {
    private:
        Node* current;
        
    public:
        Iterator(Node* current) : current(current) {}
        
        bool hasNext() const {
            return current != nullptr;
        }
        
        int next() {
            if (!hasNext()) {
                throw std::logic_error("No next element");
            }
            int data = current->data;
            current = current->next;
            return data;
        }
    };
    
    Iterator iterator() const {
        return Iterator(head);
    }
};

int main() {
    DoublyLinkedList l;
    l.append(5);
    l.addLast(10);
    l.addFirst(6);
    l.addAt(1, 15);
    
    DoublyLinkedList::Iterator it = l.iterator();
    while (it.hasNext()) {
        std::cout << it.next() << " ";
    }
    std::cout << std::endl;
    
    std::cout << l.indexOf(10) << std::endl;
    std::cout << l.contains(15) << std::endl;
    std::cout << l.contains(19) << std::endl;
    
    l.clear();
    return 0;
}