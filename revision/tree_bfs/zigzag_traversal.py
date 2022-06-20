"""
"""

from collections import deque



def traverse_zigzag(root):


    queue = deque()
    queue.append(root)
    
    results = []
    left_to_right = True
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
        if left_to_right:
            results.append(current_level)
            left_to_right = False
        else:
            results.append(current_level[::-1])
            left_to_right = True        
    return results