"""
Node Depths
Find the depth of every node and return the sum of the depths of all the nodes
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def calculate_node_depth(node, depth=0):
    """
    :@param Node node: The root node of the binary tree initially
    :return int node_depth: The total depth of the node level
    Recursive approach
    The max number of stacks on the call stack is the height of the stack, h
    h=height
    Time = O(n)
    Space = O(h)
    """
    if node is None:
        return 0
    return depth + calculate_node_depth(node.left, depth=depth+1) + calculate_node_depth(node.right, depth=depth+1)

def calculate_node_depth_alt(node):
    """
    :@param Node node: The root node of the binary tree initially
    :return int node_depth: The total depth of the node level
    Recursive approach
    The max number of stacks on the call stack is the height of the stack, h
    h=height
    Time = O(n)
    Space of the list/stack that is occupied at any time max is O(h)
    """
    node_depth = 0
    stack = [(node, 0)]
    while len(stack) > 0:
        data = stack.pop()
        curr_node, depth = data
        if curr_node is None:
            continue        
        node_depth += depth
        if not curr_node.left and not curr_node.right:
            continue
        stack.append((curr_node.left, depth+1))
        stack.append((curr_node.right, depth+1))
    return node_depth

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

    # five_node.left = ten_node
    
    res = calculate_node_depth(node=root,depth=0)
    print(f"[main] The node depth is ::: {res}")

    res = calculate_node_depth_alt(node=root)
    print(f"[main] The node depth calculated alternatively is ::: {res}")
