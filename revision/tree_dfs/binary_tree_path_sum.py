"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

"""



def has_path(root, target_sum):
    if root is None:
        return False
    
    if root.val == target_sum and root.left is None and root.right is None:
        return True
    
    return has_path(root.left, target_sum=target_sum-root.val) or has_path(root.right, target_sum=target_sum-root.val)
    
