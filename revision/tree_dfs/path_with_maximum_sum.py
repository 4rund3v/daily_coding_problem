"""
Path with Maximum Sum (hard) #
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
"""


def find_diameter(root):
    max_sum = {"max_sum": float("-inf")}
    def calculate_max_path_sum(node):
        if node is None:
            return 0

        left_tree_sum = max(calculate_max_path_sum(node.left), 0)
        right_tree_sum = max(calculate_max_path_sum(node.right), 0)
        current_path_sum = left_tree_sum + right_tree_sum + node.val

        if current_path_sum > max_sum["max_sum"]:
            max_sum["max_sum"] = current_path_sum

        return max(left_tree_sum, right_tree_sum) + node.val
    calculate_max_path_sum(root)
    return max_sum['max_sum']
