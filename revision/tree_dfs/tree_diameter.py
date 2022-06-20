"""
Tree Diameter (medium) #
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""

def find_diameter(root):
    max_height = {"max_height": 0}
    def calculate_max_height(node):
        if node is None:
            return 0
        current_diameter = left_tree_height + right_tree_height + 1
        if current_diameter > max_height["max_height"]:
            max_height["max_height"] = current_diameter

        left_tree_height = calculate_max_height(node.left)
        right_tree_height = calculate_max_height(node.right)
        return max(left_tree_height, right_tree_height) + 1
    return max_height['max_height']
    