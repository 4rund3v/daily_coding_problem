"""
Floyds tortoise and hare algorithm
Two pointers
T and H
when the tortoise and hare meet before the hare reaches null, this indicates the Cycle
when the tortoise continues to move || (paralley) will get to where the cycle beings
"""
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return fr"""<Node :: {self.value}>"""

def find_cycle(head):
    if not head:
        return None
    if not head.next:
        return None   
    tortoise = hare = head
    while hare and hare.next:
        # print(f"[find_cycle] the tortoise is at :: {tortoise.value}")
        # print(f"[find_cycle] the hare is at :: {hare.value}")
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            # both have reached the same place.
            break
    if hare != tortoise:
        # they havent met, no cycle
        return None
    node = head
    while node != tortoise:
        tortoise = tortoise.next
        node = node.next
    return tortoise

if __name__ == "__main__":
    values = list(range(10))
    nodes = [Node(value=i) for i in values]

    idx = 0

    while idx < len(nodes)-1:
        current_node = nodes[idx]
        next_node = nodes[idx+1]
        current_node.next = next_node
        idx += 1

    head = nodes[0]
    node = head
    while node:
        print(f"{node.value}",end=", ")
        node = node.next
    # introduce the cycle
    nodes[9].next = nodes[3]
    
    print()
    node = nodes[0]
    i = 11
    while i >= 0:
        print(f"{node.value}", end=", ")
        i -= 1
        node = node.next
    print()
    cycle_node  = find_cycle(head=nodes[0])
    print(f"[main] The cycle is at the node :: {cycle_node}")
