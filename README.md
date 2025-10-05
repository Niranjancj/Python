# Data Structures and Algorithms - Python Practice

A comprehensive collection of fundamental data structures and algorithms implemented in Python. This repository serves as a learning resource and reference for common DSA concepts.

## 📚 Contents

### Data Structures

#### Linear Data Structures
- **Linked List** (`linkedlist.py`) - Singly linked list implementation with operations like append, prepend, insert, remove, reverse, and swap pairs
- **Doubly Linked List** (`doublylinkedlist.py`) - Doubly linked list with bidirectional traversal
- **Stacks & Queues** (`stacks_queues.py`) - LIFO and FIFO data structure implementations

#### Non-Linear Data Structures
- **Binary Search Tree** (`BinarySearchTree.py`) - BST with insertion, deletion, search operations, and tree traversals (BFS, DFS Pre-order, In-order, Post-order)
- **Graph** (`Graph.py`) - Graph data structure implementation
- **Heap** (`Heaps.py`) - Heap data structure (Min/Max heap)

#### Hash-Based Structures
- **Hash Table** (`HashTable.py`) - Hash table implementation with collision handling

### Sorting Algorithms (`basicsorts.py`)

Implementations of fundamental sorting algorithms:

1. **Bubble Sort** - O(n²) - Simple comparison-based sorting
2. **Selection Sort** - O(n²) - Finds minimum element and swaps
3. **Insertion Sort** - O(n²) - Builds sorted array one item at a time
4. **Merge Sort** - O(n log n) - Divide and conquer approach
5. **Quick Sort** - O(n log n) average - Partition-based sorting

### Practice Files
- `practice_ll.py` - Additional linked list practice problems
- `test.py` - Testing and experimentation file

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Usage

Each file can be run independently. Simply execute the desired file:

```bash
python linkedlist.py
python BinarySearchTree.py
python basicsorts.py
```

## 💡 Key Features

### Linked List Operations
- Append, prepend, insert at index
- Pop, pop first, remove at index
- Get and set values by index
- Reverse list
- Swap adjacent pairs

### Binary Search Tree Operations
- Iterative and recursive insertion
- Iterative and recursive search (contains)
- Delete nodes
- Breadth-First Search (BFS)
- Depth-First Search (DFS): Pre-order, In-order, Post-order

### Sorting Algorithms Comparison

| Algorithm | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|-----------|----------------------|--------------------------|------------------------|------------------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

## 📖 Learning Path

Recommended order for studying:

1. **Arrays & Basic Sorting** - Start with `basicsorts.py`
2. **Linked Lists** - Move to `linkedlist.py` and `doublylinkedlist.py`
3. **Stacks & Queues** - Study `stacks_queues.py`
4. **Hash Tables** - Understand `HashTable.py`
5. **Trees** - Learn `BinarySearchTree.py` and tree traversals
6. **Heaps** - Study `Heaps.py`
7. **Graphs** - Explore `Graph.py`

## 🔍 Code Examples

### Linked List Example
```python
my_list = LinkedList(66)
my_list.append(33)
my_list.append("Python")
my_list.prepend(10)
my_list.printList()
my_list.reverse()
```

### Binary Search Tree Example
```python
bst = BinarySearchTree()
bst.r_insert(9)
bst.r_insert(4)
bst.r_insert(20)
print(bst.dfs_in_order())  # [4, 9, 20]
print(bst.BFS())  # [9, 4, 20]
```

### Sorting Example
```python
my_list = [4, 6, 1, 7, 3, 2, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)  # [1, 2, 3, 4, 5, 6, 7]
```

## 🎯 Key Concepts Covered

- **Time & Space Complexity Analysis**
- **Recursion vs Iteration**
- **Tree Traversal Techniques**
- **Sorting Algorithm Trade-offs**
- **Pointer Manipulation**
- **Object-Oriented Design**

## 📝 Notes

- All implementations include working example code at the bottom of each file
- Code is designed for learning purposes with clear, readable structure
- Some functions use both iterative and recursive approaches for comparison

## 🤝 Contributing

This is a personal learning repository. Feel free to fork and use for your own practice!

## 📄 License

This project is open source and available for educational purposes.

## 🔗 Related Topics

- Algorithm Design Patterns
- Big O Notation
- Dynamic Programming
- Greedy Algorithms
- Graph Algorithms (BFS, DFS, Dijkstra's, etc.)

---

**Happy Learning! 🚀**
