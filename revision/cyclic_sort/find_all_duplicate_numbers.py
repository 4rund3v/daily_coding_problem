"""
Problem Statement #
We are given an unsorted array containing 'n'
numbers taken from the range 1 to 'n'.
 The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def find_all_duplicate_numbers(nums):
    # sort the elements in place 
    # then find the numbers that are not in their positions and add to the duplicates
    start_pointer = 0
    while start_pointer < len(nums):
        value_at_pos = nums[start_pointer] - 1
        if nums[start_pointer] != nums[value_at_pos]:
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1
        pass

    duplicate_numbers = []
    for idx in range(len(nums)):
        if nums[idx] != idx + 1:
            duplicate_numbers.append(nums[idx])
    
    return duplicate_numbers

items = [3, 4, 5, 5, 2, 6, 2]
print(f"Items to find duplicates is :: {items}")
res = find_all_duplicate_numbers(nums=items)
print(f"Items to find duplicates is :: {items}")
print(f"Duplicate numbers are {res}")