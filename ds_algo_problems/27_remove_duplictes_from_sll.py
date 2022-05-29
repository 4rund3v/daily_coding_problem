"""
Remove duplicates from a sorted singly linked list
O(n)
"""
from singly_linked_list import SinglyLinkedList


def remove_duplicates_from_sorted_singly_linked_list(node):
    curr = node
    while curr:
        next_node = curr.next
        while next_node != None and next_node.value == curr.value:
            next_node = next_node.next
        curr.next = next_node
        curr = next_node
    print(f"[remove_duplicates_from_sorted_singly_linked_list] The nodes are cleared :: {node}")
    return node


if __name__ == "__main__":
    sll = SinglyLinkedList()
    values = [10, 11, 11, 11, 17, 18, 18, 18, 19, 19, 20, 20, 21, 21, 21 ,22, 24]
    for val in values:
        sll.add_at_tail(value=val)
    print(f"[main] the singly linked list is :: {sll}")
    remove_duplicates_from_sorted_singly_linked_list(node = sll.head)
    node = sll.head
    while node:
        print(f"{node.value}", end=",")
        node = node.next

