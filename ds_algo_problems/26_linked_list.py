"""
Singly linked list can have properties like 
> Head 
> Tail
> Length

"""

## Design a singly linked list
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"""<Node value:{self.value} has_next_node:{self.next is not None}>"""

class SinglyLinkedList:
    def __init__(self) -> None:
        """
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        """
        """
        self.is_index_valid(index=index)
        node = self.head
        i = 0
        while index > i:
            node = node.next            
            i += 1
        if i == index:
            return node
        print(f"[get] The node at index is :: index[{i}] {node}  ")
        return -1

    def add_at_head(self, value):
        node = Node(value=value)
        if self.head is None:            
            self.head = node
            self.tail = self.head
        else:
            temp = self.head
            self.head = node
            node.next = temp
        self.increment_count()
        pass
    
    def add_at_tail(self, value):
        if self.head is None:
            self.add_at_head(value=value)
        else:
            node = Node(value=value)
            temp = self.tail
            self.tail = node
            temp.next = node
            self.increment_count()
        pass

    def add_at_index(self, index, value):
        self.is_index_valid(index)
        if index == 0:
            self.add_at_head(value=value)
        if index == self.size:
            self.add_at_tail(value=value)
        
        node = Node(value=value)
        prev_node = self.get(index=index-1)
        temp = prev_node.next
        prev_node.next = node
        node.next = temp
        self.increment_count()

    def is_index_valid(self, index):
        if index < 0 or index > self.size:
            raise Exception("SinglyLinkedList-IndexError: list index out of range")

    def delete_at_index(self, index):
        self.is_index_valid(index=index)
        if index == 0:
            node_at_index = self.head
            next_node = node_at_index.next
            self.head = next_node
            if next_node is None:
                self.tail = self.head            
        elif index == self.size:
            node_at_index = self.tail
            prev_node = self.get(index=index-1)
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = self.get(index=index-1)
            node_at_index = prev_node.next
            next_node = node_at_index.next
            prev_node.next = next_node
        self.deccrement_count()
        return node_at_index

    def increment_count(self):
        self.size += 1

    def deccrement_count(self):
        self.size -= 1

    def __str__(self) -> str:
        return f'''<SinglyLinkedList : Size[{self.size}], Head[{self.head}] -> Tail[{self.tail}]>'''

if __name__ == "__main__":
    sll = SinglyLinkedList()
    values = [10, 11, 23, 34, 57, 76, 81, -1, -6, -9]
    for val in values:
        sll.add_at_tail(value=val)
    print(f"[main] the singly linked list is :: {sll}")
    sll.add_at_index(6, 66)
    print(f"[main] the singly linked list is :: {sll.get(6)}")
    sll.add_at_index(10, 99)
    print(f"[main] the singly linked list is :: {sll.get(9)}")
    sll.delete_at_index(7)
    print(f"[main] the singly linked list is :: {sll.get(9)}")