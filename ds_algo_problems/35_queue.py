"""
Queue
 -> FIFO
 -> enqueue : 
 -> dequeue
"""

class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return fr'''{self.value} -> {self.next}'''

class Queue:
    '''
    Add at the end O(1)
    Remove from the begining O(1)
    efficient
    '''
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.size = 0
        pass

    def enqueue(self, value):
        """
        Elements are added to the back of the queue
        """
        node = Node(value=value)
        if self.back is None:
            self.back = node
            self.front = node
        else:
            temp = self.back
            temp.next = node
            self.back = node
        self.size += 1
        pass

    def dequeue(self):
        """
        Elements are removed from the front of the queue
        Since we dont need to iterate over the queue
        """
        node = self.front
        temp = node.next
        self.front = temp

        self.size -= 1
        return node.value

    def __str__(self) -> str:
        return fr'''{self.front}'''

if __name__ == "__main__":
    items = [1, 2, 3, 10, 12, 15, 17, 89, 12]
    queue = Queue()
    for val in items:
        queue.enqueue(value=val)
    print(f"[main]: The queue constructed is :: {queue}")
    res = queue.dequeue()
    print(f"[main]: The dequeued elem is :: {res}")
    print(f"[main]: The queue constructed is :: {queue}")
