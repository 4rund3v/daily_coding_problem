"""
Binary Search tree
-all nodes to the left are less than the root .
-all nodes to the right are greater than the root.
 left < root < right
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return fr'''{self.left} {self.value} {self.right}'''

class BinarySearchTree():
    def __init__(self) -> None:
        pass
    def insert(self, value):
        pass
    def find(self, value):
        pass
    def remove(self, value):
        pass
