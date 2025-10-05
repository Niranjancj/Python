class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root

        while (True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __minimum_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
                
    def __r_delete(self, current_node, value):
        if current_node == None:
            return False
        if value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        else:
             if current_node.left == None and current_node.right == None:
                 return None
             elif current_node.left == None:
                 current_node = current_node.right
             elif current_node.right == None:
                 current_node = current_node.left
             else:
                 sub_tree_min = self.__minimum_value(current_node.right)
                 current_node.value = sub_tree_min
                 current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node
    
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result
    
    def dfs_pre_order(self):
        result = []

        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result
    
    def dfs_post_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)
        return result
    
    def dfs_in_order(self):
        result = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return result
        
            


my_binarytree = BinarySearchTree()
my_binarytree.r_insert(9)
my_binarytree.r_insert(10)
my_binarytree.r_insert(8)
my_binarytree.r_insert(11)
my_binarytree.r_insert(7)
my_binarytree.r_insert(12)
my_binarytree.r_insert(6)

print(my_binarytree.dfs_in_order())

        