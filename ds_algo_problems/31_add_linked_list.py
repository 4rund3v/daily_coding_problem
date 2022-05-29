"""
  540    -> 0 -> 4 -> 5
  723    -> 3 -> 2 -> 7
 - - -
 1263   3 -> 6 -> 2 -> 1

"""

from threading import local


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self) -> str:
        return fr'''{self.next} {self.value} '''

def add_linked_list(a, b):
    """
    Time O( max(m, n)) where the m and n indicate the length of the linked lists
    Space O ( max(m, n) + 1) -> O(max(m, n)) where the m and n indicate the length of the linked lists
    """
    total_sum_head= total_sum = None
    node_a = a
    node_b = b
    
    carry_over = 0
    while node_a or node_b or carry_over:
        if node_a and node_b:
            local_sum = node_a.value + node_b.value
            node_a = node_a.next
            node_b = node_b.next
        elif node_a:
            local_sum = node_a.value
            node_a = node_a.next            
        elif node_b:
            local_sum = node_b.value    
            node_b = node_b.next
        elif carry_over:
            local_sum = carry_over
            carry_over = 0
        local_sum += carry_over
        print(f"[add_linked_list] the local sum is :: {local_sum}")
        if local_sum > 9:
            local_sum = local_sum % 10
            carry_over = 1
        else:
            carry_over = 0
        node = Node(value=local_sum)
        if total_sum_head is None:
            total_sum = node
            total_sum_head = node
        else:
            total_sum.next = node
            total_sum = node
    return total_sum_head

if __name__ == "__main__":
    z = Node(0)
    z.next = Node(4)
    z.next.next = Node(5)

    t = Node(3)
    t.next = Node(2)
    t.next.next = Node(7)
    first_num = z

    second_num = t
    print(f"[main] The numbers to add are :: {z} & {t}")
    
    total = add_linked_list(a= first_num, b= second_num)
    print(f"[main] The sum of the two numbers is ::: {total}")
