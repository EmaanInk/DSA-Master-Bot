LESSONS = {
    "Arrays": {
        "level": "Beginner",
        "explanation": """
An array is the simplest data structure — a collection of elements stored in contiguous memory locations.
Think of it like a row of boxes, each numbered starting from 0.

Key properties:
- Fixed size (in most languages)
- Elements accessed by index in O(1) time
- Insertion/deletion in the middle is O(n) — everything shifts
        """,
        "code": """
# Creating and working with arrays in Python (lists)
arr = [10, 20, 30, 40, 50]

# Access by index — O(1)
print("First element:", arr[0])
print("Last element:", arr[-1])

# Insertion at end — O(1)
arr.append(60)
print("After append:", arr)

# Insertion in middle — O(n)
arr.insert(2, 99)
print("After insert at index 2:", arr)

# Deletion — O(n)
arr.remove(99)
print("After remove:", arr)

# Traversal — O(n)
for i, val in enumerate(arr):
    print(f"Index {i}: {val}")
        """,
        "practice": [
            {
                "question": "Write a function that finds the maximum element in an array without using max().",
                "hint": "Loop through the array keeping track of the largest value seen so far.",
                "solution": """
def find_max(arr):
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([3, 1, 7, 2, 9, 4]))  # Output: 9
                """
            },
            {
                "question": "Write a function that reverses an array in place without using reverse().",
                "hint": "Use two pointers — one at start, one at end, swap and move inward.",
                "solution": """
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_array([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
                """
            }
        ],
        "diagram_type": "array"
    },

    "Linked Lists": {
        "level": "Beginner",
        "explanation": """
A linked list is a chain of nodes where each node holds a value and a pointer to the next node.
Unlike arrays, elements are NOT stored in contiguous memory — they're scattered and connected by pointers.

Key properties:
- Dynamic size — grows and shrinks easily
- No random access — must traverse from head O(n)
- Insert/delete at head is O(1)
- Insert/delete in middle is O(n) to find, O(1) to do
        """,
        "code": """
# Building a Linked List from scratch
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # 10 -> 20 -> 30 -> None
        """,
        "practice": [
            {
                "question": "Write a function to find the length of a linked list.",
                "hint": "Traverse the list counting each node until you hit None.",
                "solution": """
def length(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
                """
            }
        ],
        "diagram_type": "linked_list"
    },

    "Stacks": {
        "level": "Beginner",
        "explanation": """
A stack follows LIFO — Last In, First Out.
Think of a stack of plates. You always add and remove from the top.

Operations:
- push(x) — add to top — O(1)
- pop() — remove from top — O(1)
- peek() — look at top without removing — O(1)

Real world uses: undo/redo, browser back button, function call stack
        """,
        "code": """
# Stack implementation using Python list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Top:", s.peek())   # 3
print("Pop:", s.pop())    # 3
print("Top:", s.peek())   # 2
        """,
        "practice": [
            {
                "question": "Use a stack to check if a string of brackets is balanced. E.g. '([{}])' is valid, '([)]' is not.",
                "hint": "Push opening brackets. When you see a closing bracket, pop and check if it matches.",
                "solution": """
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("([{}])"))  # True
print(is_balanced("([)]"))    # False
                """
            }
        ],
        "diagram_type": "stack"
    },

    "Queues": {
        "level": "Beginner",
        "explanation": """
A queue follows FIFO — First In, First Out.
Think of a line at a ticket counter. First person in line is first to be served.

Operations:
- enqueue(x) — add to back — O(1)
- dequeue() — remove from front — O(1)
- peek() — look at front — O(1)

Real world uses: task scheduling, printer queues, BFS graph traversal
        """,
        "code": """
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
q.enqueue("Task 1")
q.enqueue("Task 2")
q.enqueue("Task 3")
print("Front:", q.peek())      # Task 1
print("Dequeue:", q.dequeue()) # Task 1
print("Front:", q.peek())      # Task 2
        """,
        "practice": [
            {
                "question": "Implement a queue using two stacks.",
                "hint": "Use one stack for enqueue, one for dequeue. When dequeue stack is empty, pour everything from enqueue stack into it.",
                "solution": """
class QueueUsingStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop() if self.outbox else "Empty"

q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.dequeue())  # 2
                """
            }
        ],
        "diagram_type": "queue"
    },

    "Binary Trees": {
        "level": "Intermediate",
        "explanation": """
A binary tree is a hierarchical structure where each node has at most two children — left and right.

Key terms:
- Root: the top node
- Leaf: a node with no children
- Height: longest path from root to a leaf
- Depth: distance from root to a node

Traversals:
- Inorder (Left, Root, Right) — gives sorted output for BST
- Preorder (Root, Left, Right)
- Postorder (Left, Right, Root)
        """,
        "code": """
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

# Build a tree
#        1
#       / \\
#      2   3
#     / \\
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bt = BinaryTree()
bt.root = root

print("Inorder:")  # 4 2 5 1 3
bt.inorder(bt.root)
print("\\nPreorder:") # 1 2 4 5 3
bt.preorder(bt.root)
        """,
        "practice": [
            {
                "question": "Write a function to find the height of a binary tree.",
                "hint": "Height = 1 + max(height of left subtree, height of right subtree). Base case: None node has height 0.",
                "solution": """
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

print(height(root))  # 3
                """
            }
        ],
        "diagram_type": "binary_tree"
    },

    "Binary Search": {
        "level": "Intermediate",
        "explanation": """
Binary search finds an element in a SORTED array by repeatedly halving the search space.

Instead of checking every element (O(n)), you check the middle:
- If middle == target, found it
- If middle > target, search left half
- If middle < target, search right half

Time complexity: O(log n) — incredibly fast
Space complexity: O(1) iterative, O(log n) recursive
        """,
        "code": """
# Iterative binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid          # Found at index mid
        elif arr[mid] < target:
            left = mid + 1      # Search right half
        else:
            right = mid - 1     # Search left half

    return -1  # Not found

arr = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91]
print(binary_search(arr, 23))   # Output: 5
print(binary_search(arr, 100))  # Output: -1

# Recursive version
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
        """,
        "practice": [
            {
                "question": "Given a sorted array, find the first occurrence of a target element (there may be duplicates).",
                "hint": "Modified binary search — when you find the target, don't stop. Keep searching left.",
                "solution": """
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

print(first_occurrence([1, 2, 2, 2, 3, 4], 2))  # Output: 1
                """
            }
        ],
        "diagram_type": "binary_search"
    }
}

LEVEL_ORDER = ["Beginner", "Intermediate", "Advanced"]

TOPIC_ORDER = [
    "Arrays",
    "Linked Lists",
    "Stacks",
    "Queues",
    "Binary Search",
    "Binary Trees",
]