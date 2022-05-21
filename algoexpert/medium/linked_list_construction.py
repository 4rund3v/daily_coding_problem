"""
Construct a linked list
    : prev and next pointers
Doubly linked list :  the head and the tail


Write a class for a Doubly Linked List.
 -The class should have a "head" and "tail" properties,
  both of which should point to either the None (null) value or to a Linked List node.
- Every node will have a "value" property as well as "next" and "prev" properties,
  both of which can point to either the None (null) value or another node.
- The class should support setting the head and tail of the linked list,
  inserting nodes before and after other nodes as well as at certain positions,
  removing given nodes and removing nodes with specic values, and searching for nodes with values.
- Only the searching method should return a value: specically, a boolean.

Sample input: 1 -> 2 -> 3 -> 4 -> 5
Sample output (after setting 4 to head): 4 -> 1 -> 2 -> 3 -> 5
Sample output (after setting 6 to tail): 4 -> 1 -> 2 -> 3 -> 5 -> 6
Sample output (after inserting 3 before 6): 4 -> 1 -> 2 -> 5 -> 3 -> 6
Sample output (after inserting a new 3 after 6): 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3 
Sample output (after inserting a new 3 at position 1): 3 -> 4 -> 1 -> 2 -> 5 -> 3 -> 6 -> 3
Sample output (after removing nodes with value 3): 4 -> 1 -> 2 -> 5 -> 6
Sample output (after removing 2): 4 -> 1 -> 5 -> 6
Sample output (after searching for 5): True

Explanation
We can use a Stack here

"""

from unicodedata import name


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self) -> str:
        node = self.head
        paths = []
        while node!= None:
            paths.append(str(node.value))
            node = node.next
        return r''' -> '''.join(paths)

    def set_head(self, node):
        if self.head:
            self.insert_before(existing_node=self.head, new_node=node)
        else:
            self.head = node
            self.tail = node

    def set_tail(self, node):
        if self.tail:
            self.insert_after(existing_node=self.tail, new_node=node)
        else:
            self.set_head(node)

    def insert_before(self, existing_node, new_node):
        if new_node == self.head and new_node == self.tail:
            # indicates the head/tail node
            return
        # in case this is a existing new that is being inserted before an node.
        self.remove_node_bindings(new_node)
        new_node.prev = existing_node.prev
        new_node.next = existing_node
        if existing_node.prev is None:
            self.head = new_node
        else:
            existing_node.prev.next = new_node
        existing_node.prev = new_node
        pass

    def insert_after(self,  existing_node, new_node):
        if new_node == self.head and new_node == self.tail:
            # indicates the head/tail node
            return
         # in case this is a existing new that is being inserted before an node.
        self.remove_node_bindings(new_node)
        new_node.prev = existing_node
        new_node.next = existing_node.next
        if existing_node.next is None:
            self.tail = new_node
        else:
            existing_node.next.prev = new_node
        existing_node.next = new_node
        pass

    def insert_at_position(self, position, new_node):
        if position == 1:
            self.set_head(new_node)
            return
        node = self.head
        current_pos = 1
        while node != None and current_pos != position:
            node = node.next
            current_pos += 1
        if node is not None:
            self.insert_before(node, new_node=new_node)
        else:
            self.set_tail(node=new_node)

    def remove_nodes_with_value(self, value):
        node = self.head
        while node != None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node=node_to_remove)
        pass

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.remove_node_bindings(node)
        pass

    def remove_node_bindings(self, node):
        """
        Ensure that the nodes pervious and next pointers are appropriately moved
        """
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def contains_node_with_value(self, value):
        """
        Check if a value is present in the linked list
        """
        node = self.head
        while node != None and node.value != value:
            node = node.next
        return node.value == value

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.set_tail(Node("1"))
    doubly_linked_list.set_tail(Node("2"))
    doubly_linked_list.set_tail(Node("3"))
    doubly_linked_list.set_tail(Node("4"))
    doubly_linked_list.set_tail(Node("5"))
    print(f"The doubly linked list prepared is :: {doubly_linked_list}")
    doubly_linked_list.set_head(node=Node(value=4))
    print(f"The doubly linked list prepared is :: {doubly_linked_list}")
    doubly_linked_list.set_head(node=Node(value=6))
    print(f"The doubly linked list prepared is :: {doubly_linked_list}")
    doubly_linked_list.remove(doubly_linked_list.tail)
    print(f"The doubly linked list prepared is :: {doubly_linked_list}")


