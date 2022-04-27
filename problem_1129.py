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
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = ''
        self.right = ''

    def __str__(self):
        return f"""{self.left} - {self.data} - {self.right}"""

def reconstruct_tree(preorder, inorder, start, end):
    """
    Reconstructs the tree recursively, 
    taking the root order from the preorder traversal
    and the subtress from the inorder traversals
    """
    global tree_index

    node = Node(preorder[tree_index])
    tree_index += 1

    if start == end:
        return node

    root_index = inorder.index(node.data)
    node.left = reconstruct_tree(preorder, inorder, start=start, end=root_index-1)
    node.right = reconstruct_tree(preorder, inorder, start=root_index+1, end=end)
    return node


if __name__ == "__main__":
    # left -> root -> right
    inorder  = ["d", "b", "e", "a", "f", "c", "g"]
    # # root -> left -> right
    preorder = ["a", "b", "d", "e", "c", "f", "g"]

    tree_index = 0
    tree = reconstruct_tree(preorder=preorder, inorder=inorder, start=0, end=len(inorder)-1)
    print(f"[main] The tree created is :: {tree}")