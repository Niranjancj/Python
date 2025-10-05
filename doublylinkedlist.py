class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def setvalue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.get(index - 1)
            current = temp.next
            temp.next = new_node
            new_node.prev = temp
            current.prev = new_node
            new_node.next = current
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.popfirst()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp


    def reversebetween(self, start, end):
        if self.length <= 1 or start == end:
            return None
        
        d1 = Node(0)
        d1.next = self.head
        self.head.prev = d1
        temp = d1

        for _ in range(start):
            temp = temp.next

        current = temp.next

        for _ in range(end - start):
            tomove = current.next
            current.next = tomove.next
            if tomove.next:
                tomove.next.prev = current
            tomove.next = temp.next
            current.prev = tomove
            temp.next = tomove
            tomove.prev = temp

        d1.next = None
        self.head.prev = None

    def swap_pairs(self):
        if self.length <= 1:
            return None
        
        d1 = Node(0)
        d1.next = self.head
        temp = d1
        
        while self.head and self.head.next:
            first = self.head
            second = self.head.next
            temp.next = second
            first.next = second.next
            second.next = first
            second.prev = temp
            first.prev = second
            if first.next:
                first.next.prev = first
            self.head = first.next
            temp = first      

        self.head = d1.next
        if self.head:
            self.head.prev = None

            
        

        

        
     

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(100)
my_doubly_linked_list.prepend(200)
my_doubly_linked_list.prepend(300)
my_doubly_linked_list.append(400)
my_doubly_linked_list.append(500)
my_doubly_linked_list.append(600)
my_doubly_linked_list.print_list()
my_doubly_linked_list.swap_pairs()
my_doubly_linked_list.print_list()




