"""
Problem Statement #
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

def cyclic_sort(nums):
    # Given numbers are unique and in range of 1-n
    # Sort the nums in a single pass,
    # In Place
    # Start by swapping the items at the start position to their correct position
    # Move start to the next position when the item at the start position matches its index
    start_pointer = 0 
    while start_pointer < len(nums):
        swap_pos = nums[start_pointer] - 1
        # Move ahead condition
        if nums[start_pointer] == nums[swap_pos]:
            start_pointer += 1
            continue
        print(f"Performing swap --> {start_pointer} {nums}")
        nums[start_pointer], nums[swap_pos] = nums[swap_pos], nums[start_pointer]
    return nums

items = [3, 1, 6, 2, 4, 5, 7, 9, 8]
print(f"The unsorted items are :: {items}")
cyclic_sort(nums=items)
print(f"The sorted items are :: {items}")
