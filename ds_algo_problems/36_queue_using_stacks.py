"""
Implement a queue using 2 stack
push(value) -> just appending to the in stack, O(1)
pop()   -- \
            > Both of these are amortized to O(1), since there are 1 O(n)operations, + (n-1)O(1) averages out it will be O(1)
peek()  -- /
           n Operations = O(n)
           n = n*O(1)
           averages -> O(1)

empty() -> return True if the instack and outstack is empty else False ( O(1) )
"""


class StackQueue():
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []

    def push(self, value):
        self.in_stack.append(value)
    
    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        elem = self.out_stack.pop()
        return elem

    def empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        elem = self.out_stack[-1]
        return elem