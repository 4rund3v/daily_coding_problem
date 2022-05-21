""" 
# BRANCH SUMS
Write a function that takes in a Binary Tree and
returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch.
A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. 
"""


def calculate_branch_sum(node):
    """
    finds the branch sums in a binary tree ( left and right node)
    branch sums is the sums from the root to the leaf node;
    :@param Node node: The root of the binary tree
    :return [] branch_sums : The array containing the branch sums of the array
    Recursive approach
    for each node, keep travesing till the leaf and get its sum
        ex: input 
                      1
                    /   \
                 2        3
                / \      /  \ 
              4     5   6    7
            /   \     \
          8       9    10

        output : [ 15, 16, 18, 10, 11]
    Complexity:
    Average Case:
       Time: O(N) all leaves are traversed, Space O(N) 
    """
    branch_sums= []
    def helper(node, current_sum, branch_sums):
        if node is None:
            return
        current_sum += node.value
        if not node.left and not node.right:
            branch_sums.append(current_sum)
            return
        helper(node=node.left, current_sum=current_sum, branch_sums=branch_sums)
        helper(node=node.right, current_sum=current_sum, branch_sums=branch_sums)

    helper(node, 0, branch_sums)
    return branch_sums


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(value = 1)
    two_node = Node(value=2)
    three_node = Node(value=3)
    four_node = Node(value=4)
    five_node = Node(value=5)
    six_node = Node(value=6)
    seven_node = Node(value=7)
    eight_node = Node(value=8)
    nine_node = Node(value=9)
    ten_node = Node(value=10)

    root.left = two_node
    root.right = three_node
    
    two_node.left = four_node
    two_node.right = five_node
    
    three_node.left = six_node
    three_node.right = seven_node

    four_node.left = eight_node
    four_node.right = nine_node

    five_node.left = ten_node

    res = calculate_branch_sum(node=root)
    print(f"[main] The branch sum calculated is :: {res}")