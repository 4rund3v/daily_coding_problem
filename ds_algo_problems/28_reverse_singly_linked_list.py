"""
Reverse the singly linked list
"""
from singly_linked_list import SinglyLinkedList


def reverse_singly_linked_list(node):
    """
    1 -> 2 -> 3 -> 4
    null <- 1 <- 2 <- 3 <- 4
    """
    current = node
    prev = None
    while current:
        next_node  = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


if __name__ == "__main__":
    sll = SinglyLinkedList()
    values = [10, 11, 11, 11, 17, 18, 18, 18, 19, 19, 20, 20, 21, 21, 21 ,22, 24]
    for val in values:
        sll.add_at_tail(value=val)
    print(f"[main] the singly linked list is :: {sll}")
    head = reverse_singly_linked_list(node=sll.head)
    node = head
    while node:
        print(f"{node.value}", end=",")
        node = node.next