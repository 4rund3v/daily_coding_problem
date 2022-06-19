"""
Problem Statement #
We are given an array containing `n` distinct numbers taken from the range 0 to `n`.
 Since the array has only `n` numbers out of the total `n+1` numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""

def find_missing_numbers(nums):
    # First sort the numbers and find the first missing number
    # sort the numbers in place in O(n) 
    # by swapping the positions of the numbers to their index
    start_pointer = 0
    total_len = len(nums)
    while start_pointer < total_len:
        value_at_pos = nums[start_pointer]
        if nums[start_pointer] < total_len and nums[start_pointer] != nums[value_at_pos]:
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1
    # find the first missing number
    for idx in range(total_len):
        if nums[idx] != idx:
            return idx
    return total_len

items = [4, 0, 3, 1]
print(f"The unsorted items are :: {items}")
res = find_missing_numbers(nums=items)
print(f"The missing number is  :: {res}")