"""
Depth First Search
Problem Statement
You are given a Node class that has a name and an array of optional children Nodes.
When put together, Nodes form a simple tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array,
traverses the tree using the Depth-rst Search approach (specically navigating the tree from left to right), stores all the of the Nodes' names in the input array, and returns it.

Sample input: 
            A
          / | \
        B   C   D
       / \     /  \
      E   F   G    H 
         / \   \
        I   J   K
Sample output: ["A","B","E","F","I","J","C","D","G","K","H"]
"""



class Node():
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        pass

    def add_child(self, child) -> None:
        self.children.append(child)

    def depth_first_search(self, array):
        """
        The time complexity ( every node is visited(V) + every child is itterated by its edges(E) ) = O(V+E)
        Space is : The returning array is going to contain only ( V) O(V)
                also counting the number of frames at any point is going to be maximum of (V)
        """
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array=array)
        return array

if __name__ == "__main__":
    root = Node(name="A")
    r_node = Node(name="R")
    u_node = Node(name="U")
    n_node = Node(name="N")
    d_node = Node(name="D")
    e_node = Node(name="E")
    v_node = Node(name="V")
    p_node = Node(name="P")

    root.add_child(r_node)
    r_node.add_child(u_node)
    u_node.add_child(n_node)
    root.add_child(d_node)
    d_node.add_child(e_node)
    e_node.add_child(v_node)
    root.add_child(p_node)
    
    res = root.depth_first_search(array=[])
    print(f"The result of the depth first search is ::: {res}")
