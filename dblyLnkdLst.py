class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if (self.size == 0):
            return True
        else:
            return False
        #return size == 0

    def __reversed__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.prev
            
    def addFirst(self, element): 
        new_node = Node(element)
        if self.isEmpty(): # if list is empty, sets head and tail to new node.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("listg is empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1

    def removeLast(self):
        if self.isEmpty():
            raise Exception("list is empty")
        else:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1

    def add(self, element, index):
        if index < 0 or index > self.size:
            raise Exception("index not in range")
        elif index == 0:
            self.addFirst(element)
        elif index == self.size:
            self.addLast(element)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(element)
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    def remove(self, index): #self, element, index
        if index < 0 or index >= self.size:
            raise Exception("index not in range")
        elif index == 0:
            self.removeFirst()
        elif index == self.size - 1:
            self.removeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current.data) + "\n"
            current = current.next
        return output

    def __eq__(self, other):
        if type(other) is not DoublyLinkedList:
            return False
        if self.size != other.size:
            return False
        current_self = self.head
        current_other = other.head
        while current_self:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

#append other to the end of the doubly linked list sekf
    def __add__(self, other):
        if type(other) is not DoublyLinkedList:
            raise Exception("The operand should be instance of doublylinkedlist")
        new_list = DoublyLinkedList()
        current_self = self.head
        while current_self:
            new_list.addLast(current_self.data)
            current_self = current_self.next
        current_other = other.head
        while current_other:
            new_list.addLast(current_other.data)
            current_other = current_other.next
        return new_list

    def __len__(self):
        return self.size
