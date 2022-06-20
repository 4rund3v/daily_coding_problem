"""
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
"""


def find_sum_of_path_numbers(root):
    def helper(node, current_path_sum):
        if node is None:
            return 0
        current_path_sum = 10*current_path_sum + node.val
        return (helper(node.left, current_path_sum) + 
               helper(node.right, current_path_sum))
        
    res = helper(root, 0)        
    return res