class Node:
    def __init__(self, data):
        self.data = data

class Stack:
    def __init__(self, max_size):
        self.head = None
        self.max_size = max_size
        self.current_size = 0
    def push(self, data):
        if self.max_size == self.current_size: return 
        self.current_size += 1
        node = Node(data)
        aux = self.head
        self.head = node
        self.head.next = aux
    def pop(self):
        if self.current_size == 0: return
        self.current_size -= 
        



        