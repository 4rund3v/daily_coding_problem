"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque



def traverse(root):


    queue = deque()
    queue.append(root)
    
    results = []
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            current_level.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        results.append(current_level)
    return results
