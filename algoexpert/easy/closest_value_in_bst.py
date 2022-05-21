"""
Find Closest Value In BST
Problem Statement
You are given a BST data structure consisting of BST nodes. 
Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right,"
 respectively.
A node is said to be a BST node if and only if it satises the BST property:
 -  its value is strictly greater than the values of every node to its left;
 -  its value is less than or equal to the values of every node to its right; 
 and both of its children nodes are either BST nodes themselves or None (null) values.
You are also given a target integer value; write a function that nds the closest value to that target value contained in the BST.

Assume that there will only be one closest value.

Sample input: target is 12 ,
tree is 
                10
              /   \
             5     15
            / \   / \
           2   5 13 22
          /        \
         1          14
Sample output: 13

Explanation
We can use a Stack here

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value=value)
            else:
                self.left.insert(value=value)
        else:
            if self.right is None:
                self.right = Node(value=value)
            else:
                self.right.insert(value=value)
        return self

def find_closest_value_in_bst(tree, target):
    return find_closest_value_in_bst_helper(tree, target, closest=float("inf"))

def find_closest_value_in_bst_helper(tree, target, closest):
    """
    Find the closest value to an given number in a BST.
    :@param BST node tree: The node of the BST tree, initially the root node
    :@param int target: The target number we are trying to find the closest value to
    :@param closest : The closest value
    :return int : The closest value
    Recursive Approach
    Average Case
    Time : O(lg(n)) on average, Space : O(lg(N)) ( for  the frames on the call stack)
    Worst case:
    when only branch is there 10 -> 15 -> 20 -> 30 ( no split/branching occurs)
    Time : O(N) on average, Space : O(N) ( for  the frames on the call stack)
    """
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest

def find_closest_value_in_bst_helper_alt(tree, target, closest):
    """
    Find the closest value to an given number in a BST.
    :@param BST node tree: The node of the BST tree, initially the root node
    :@param int target: The target number we are trying to find the closest value to
    :@param closest : The closest value
    :return int : The closest value
    Itterative Approach
    Average Case
    Time : O(lg(n)) on average, Space : O(1) 
    Worst case:
    when only branch is there 10 -> 15 -> 20 -> 30 ( no split/branching occurs)
    Time : O(N) on average, Space : O(1)
    """
    current_node = tree
    while current_node != None:    
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = tree.left
        elif target > tree.value:
            current_node = tree.right
        else:
            break
    return closest


if __name__ == "__main__":
    root = Node(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(5)
    root.insert(13)
    root.insert(22)
    root.insert(1)
    root.insert(14)
   
    res = find_closest_value_in_bst(tree=root, target=12)
    print(f"[main] The closest value found in the bst is :: {res}")