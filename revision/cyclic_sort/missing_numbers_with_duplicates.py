"""
Problem Statement #
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
"""


def find_missing_numbers(nums):
    print(f"find_missing_numbers the nums is :: {nums}")
    start_pointer = 0
    while start_pointer < len(nums):
        value_at_pos = nums[start_pointer] - 1
        if nums[start_pointer] != nums[value_at_pos]:
            print(f"Swapping :: {start_pointer} -> {value_at_pos} [{nums[start_pointer]} - {nums[value_at_pos]}]")
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1
    print(f"find_missing_numbers:: The sorted list of numbers are :: {nums}")
    missing_numbers = []
    for idx in range(len(nums)):
        if nums[idx] != idx + 1:
            missing_numbers.append(idx + 1)
    return missing_numbers

items = [2, 3, 8, 1, 2, 3, 5, 1]
res = find_missing_numbers(nums=items)
print(f"The missing numbers are :: {res}")