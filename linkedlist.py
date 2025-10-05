class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('\n')

    def append(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1
        return True
    
    def pop(self):
        pre = self.head
        temp = self.head
        if self.length == 0:
            return None
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
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
        
    def get(self, index):
        if (index < 0 or index > self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def setvalue(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insertvalue(self, index, value):
        if (index < 0 or index > self.length):
            return False
        elif (index == 0):
            return self.prepend(value)
        elif (index == self.length):
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return False
        
    def removevalue(self, index):
        if (index < 0 or index > self.length):
            return None
        elif (index == 0):
            return self.popfirst()
        elif (index == self.length):
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def swap_pairs(self):
            
            dummy_node = Node(0)
            dummy_node.next = self.head
            prev = dummy_node
            first = self.head
            
            while first and first.next:
                second = first.next
                prev.next = second
                first.next = second.next
                second.next = first
                prev = first
                first = first.next
                
            self.head = dummy_node.next

my_LinkedList1 = LinkedList(66)
my_LinkedList1.append(33)
my_LinkedList1.append("Python")
my_LinkedList1.append("Hi")
my_LinkedList1.append(77)
my_LinkedList1.append(88)
my_LinkedList1.printList()
my_LinkedList1.pop()
my_LinkedList1.printList()

