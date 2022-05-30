"""
Implement a stack
LIFO

Insert
Remove



implementing using a array
a = list()
a.push()
a.pop()
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    def __str__(self):
        return fr'''({self.value}) -> {self.next}'''


class LinkedList():
    '''
    LIFO
    add at the beginning
    remove from the begining
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            self.size += 1
        self.size += 1

    def add_at_begining(self, node):
        if self.head is None:
            self.add_at_head(node)
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            self.size += 1

    def remove_from_begining(self):
        if self.head is None:
            return Exception("IndexError: pop from empty LL.")
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return temp

    def push(self, value):
        node = Node(value)
        self.add_at_begining(node)

    def pop(self):
        node = self.remove_from_begining()
        if node is not None:
            return node.value
        return None
    
    def __str__(self) -> str:
        return fr'''{self.head} -> '''

if __name__ == "__main__":
    values = [10 ,1, 3,4,4,6,78,232, 123, 123, 1]
    stack = LinkedList()
    for val in values:
        stack.push(value=val)
    print(f"[main] The stack is ---> {stack}")
    item = stack.pop()
    print(f"[main] The recently poped item is :: {item}")
    print(f"[main] The stack is ---> {stack}")
    item = stack.pop()
    print(f"[main] The recently poped item is :: {item}")
    print(f"[main] The stack is ---> {stack}")