"""
Doubly Linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self) -> str:
        return fr'''<Node {self.value}> -> {self.next}'''

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        return fr'''{self.head}'''

    def add_at_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            temp.prev = self.head

    def add_at_tail(self, node):
        if self.head is None:
            self.add_at_head(node)
        else:
            temp = self.tail
            self.tail = node
            node.prev = temp
            temp.next = node
    
    def remove_node(self, node):
        if node is self.head:
            self.remove_head()
        elif node is self.tail:
            self.remove_tail()
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
    
    def remove_tail(self):
        if not self.tail:
            raise Exception("DoublyLinkedList: Tail not initilized, cannot remove")
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
    
    def remove_head(self):
        if not self.head:
            raise Exception("DoublyLinkedList: Head not initilized, cannot remove")
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head

    def add_node_after(self, prev_node, new_node):
        if prev_node is self.tail:
            self.add_at_tail(new_node)
        else:
            next_node = prev_node.next
            
            prev_node.next = new_node
            next_node.prev = new_node

            new_node.prev = prev_node
            new_node.next = next_node
        pass

    def add_node_before(self, next_node, new_node):
        if next_node is self.head:
            self.add_at_head(new_node)
        else:
            prev_node = next_node.prev
            
            prev_node.next = new_node
            next_node.prev = new_node

            new_node.prev = prev_node
            new_node.next = next_node
        pass
    
    def insert_postition(self, pos, node):
        pass
    def delete_at_postition(self, pos):
        pass
if __name__ == "__main__":
    values = [ 5, 7, 3, 1, 3, 2, 6]
    nodes = [Node(value=i) for i in values]
    dll = DoublyLinkedList()
    for node in nodes:
        dll.add_at_tail(node=node)
    print(f"[Main] The constructed doubly linked list is :: {dll}")
    dll.add_node_after(nodes[3], new_node=Node(114))
    print(f"[Main] The constructed doubly linked list is :: {dll}")
    dll.add_node_before(nodes[2], new_node=Node(16))
    print(f"[Main] The constructed doubly linked list is :: {dll}")