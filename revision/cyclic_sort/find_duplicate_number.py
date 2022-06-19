"""
Problem Statement #
We are given an unsorted array containing `n+1` numbers taken from the range 1 to `n`.
 The array has only one duplicate but it can be repeated multiple times.
  Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""


def find_duplicate_number(nums):
    start_pointer = 0
    while start_pointer < len(nums): 
        if nums[start_pointer] != start_pointer + 1:
            value_at_pos = nums[start_pointer] - 1
            if nums[start_pointer] != nums[value_at_pos]:
                nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
            else:
                return nums[start_pointer]
        else:
            start_pointer += 1
    return -1

items = [1, 4, 4, 3, 2]
print(f"Items to find duplicates is :: {items}")
res = find_duplicate_number(nums=items)
print(f"Items to find duplicates is :: {items}")
print(f"Duplicate number is {res}")