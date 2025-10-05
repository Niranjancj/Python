class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        print('\n')

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
            return temp

class queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
        print('\n')

    def enqueue(self, value):
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        temp = self.first
        if not self.first:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1 
        return temp        
    
    
        

my_queue = queue(7)
my_queue.print_queue()
my_queue.enqueue(11)
my_queue.enqueue(12)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
print(my_queue.dequeue())
