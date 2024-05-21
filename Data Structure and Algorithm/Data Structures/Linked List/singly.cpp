#include <iostream>

class Node {
public:
    int data;
    Node* next;
    
    Node(int data, Node* next = nullptr) : data(data), next(next) {}
};

class SinglyLinkedList {
private:
    int size;
    Node* head;
    
public:
    SinglyLinkedList() : size(0), head(nullptr) {}
    
    ~SinglyLinkedList() {
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
            head = new Node(data);
        } else {
            Node* curr = head;
            while (curr->next != nullptr) {
                curr = curr->next;
            }
            curr->next = new Node(data);
        }
        size++;
    }
    
    void addLast(int data) {
        append(data);
    }
    
    void addFirst(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
        size++;
    }
    
    void addAt(int index, int data) {
        if (index < 0 || index > size) {
            throw std::out_of_range("Index out of range");
        }
        if (index == 0) {
            addFirst(data);
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            Node* newNode = new Node(data, curr->next);
            curr->next = newNode;
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
    Node* curr = head;
    while (curr->next != nullptr) {
        curr = curr->next;
    }
    return curr->data;
}

    void removeFirst() {
        if (isEmpty()) {
            throw std::logic_error("List is empty");
        }
        Node* temp = head;
        head = head->next;
        delete temp;
        size--;
    }
    void removeLast() {
    if (isEmpty()) {
        throw std::logic_error("List is empty");
    }
    if (head->next == nullptr) {
        delete head;
        head = nullptr;
        size = 0;
        return;
    }
    Node* prev = nullptr;
    Node* curr = head;
    while (curr->next != nullptr) {
        prev = curr;
        curr = curr->next;
    }
    prev->next = nullptr;
    delete curr;
    size--;
}

    
    void removeAt(int index) {
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of range");
        }
        if (index == 0) {
            removeFirst();
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            Node* temp = curr->next;
            curr->next = temp->next;
            delete temp;
            size--;
        }
    }
    
    int indexOf(int data) const {
        Node* curr = head;
        int index = 0;
        while (curr != nullptr) {
            if (curr->data == data) {
                return index;
            }
            curr = curr->next;
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
    
    void printList() const {
        Node* curr = head;
        while (curr != nullptr) {
            std::cout << curr->data << " ";
            curr = curr->next;
        }
        std::cout << std::endl;
    }
};

int main() {
    SinglyLinkedList l;
    l.append(5);
    l.addLast(10);
    l.addFirst(6);
    l.addAt(1, 15);
    
    l.printList();
    
    std::cout << l.indexOf(10) << std::endl;
    std::cout << l.contains(15) << std::endl;
    std::cout << l.contains(19) << std::endl;
    
    l.clear();
    return 0;
}