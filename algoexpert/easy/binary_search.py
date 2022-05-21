"""
Problem Statement
Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to nd if the target number is contained in the array and should return its index if it is, otherwise -1.

Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33

Sample output: 3

Explanation
We can use a Stack here

"""
"""
SORTED LISTS -> BINARY SEARCH
"""

def binary_search(arr, num):
    """
    Recursive Approach:
    In this case we are using the same array , not keepig a copy each recursion call.
    Time : O(lg N)
    Space : O(1g N)
    """
    def binary_search_helper(arr, num, start, end):
        """
        Base Case :
         if the start > end ( when the number is not found)
        recursive case
        """
        if start > end:
            return -1
        # to indicate that to prevent overflow
        # mid = start + (end-start) // 2
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
        return binary_search_helper(arr, num, start, end)
    index = binary_search_helper(arr, num, start=0, end=len(arr)-1)    
    return index

def binary_search_alt(arr, num):
    """
    Itterative Approach:
    In this case we are using the same array , not keepig a copy each recursion call.
    Time : O(lg N)
    Space : O(1) no extra space in the call stack utilized.
    """
    start = 0
    end = len(arr)-1
    while start <= end:
        """
        Base Case :
         if the start > end ( when the number is not found)
        recursive case
        """
        # to indicate that to prevent overflow
        # mid = start + (end-start) // 2
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    a = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    num = 33
    res = binary_search(a, num)
    print(f"[main] The index of where the postion is at ::: {res}")
    num = 103
    res = binary_search(a, num)
    print(f"[main] The index of where the postion is at ::: {res}")
    num = 73
    res = binary_search(a, num)
    print(f"[main] The index of where the postion is at ::: {res}")

    num = 33
    res = binary_search_alt(a, num)
    print(f"[main] ALTERNATIVE The index of where the postion is at ::: {res}")
    num = 103
    res = binary_search_alt(a, num)
    print(f"[main] ALTERNATIVE The index of where the postion is at ::: {res}")
    num = 73
    res = binary_search_alt(a, num)
    print(f"[main] ALTERNATIVE The index of where the postion is at ::: {res}")