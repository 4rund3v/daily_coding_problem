"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g



preorder traversal - > root -> left -> right
inorder traversal - > left -> root -> right
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = ''
        self.right = ''

    def __str__(self):
        return f""" {self.left} - {self.data} - {self.right}"""

def reconstruct_tree(inorder, preorder, start, end):
    """
     1st recursion call ( post tree_index - 1)
            inorder; preorder; start; end;
            [b, a ,c]  [a, b, c]  0     2
        left subtree (root_index -> 1) ( post tree_index - 2)
            [b, a ,c]  [a, b, c]  0      0 
        right subtree ( root_index ->1 )   ( post tree_index - 3)
            [b, a ,c]  [a, b, c]  2      2
    """
    global tree_index
    print(f"[reconstruct_tree] the start , end and the tree index before access is : [{start}], [{end}], [{tree_index}]")

    # preorder used to find root elements
    node = Node(preorder[tree_index])
    tree_index += 1
    # indicates the leaf node
    if start == end:
        return node

    root_index = inorder.index(node.data)
    node.left = reconstruct_tree(inorder, preorder, start=start, end=root_index-1)
    node.right = reconstruct_tree(inorder, preorder,start=root_index+1, end=end)

    return node


if __name__ == "__main__":
    inorder = ["d", "b", "e", "a","f", "c", "g"] # [d, b, e, a, f, c, g]
    preorder = ["a", "b", "d", "e",  "c", "f", "g"] # [a, b, d, e, c, f, g]
    tree_index = 0

    tree = reconstruct_tree(inorder, preorder, start=0, end=len(inorder)-1)
    print(f"[main] The tree constructed is ::: {tree}")
    print(f"[main] The inorder traversal is ::: {inorder}")