class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print('\n')

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return temp.value
    
    def setvalue(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def reversebetween(self, start, end):
        if self.length < 1:
            return
        d1 = Node(0)
        d1.next = self.head
        temp = d1

        for _ in range (start):
            temp = temp.next
        
        current = temp.next
        
        for _ in range(end - start):
            tomove = current.next
            current.next = tomove.next
            tomove.next = temp.next
            temp.next = tomove

        self.head = d1.next




my_linked_list = LinkedList(8)
my_linked_list.append(9)
my_linked_list.append(99)
my_linked_list.append(90)
my_linked_list.prepend(33)
my_linked_list.append(900)
my_linked_list.print_list()
my_linked_list.reversebetween(1,3)
my_linked_list.print_list()
