"""
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4

Example 3:
Input: [3, 2, 5, 1]
Output: 4
"""

def find_first_missing_positive_number(nums):
    start_pointer = 0
    total_len = len(nums)
    while start_pointer < total_len:
        print(start_pointer)
        value_at_pos = nums[start_pointer] - 1
        if nums[start_pointer] > 0 and nums[start_pointer] <= total_len and nums[start_pointer] != nums[value_at_pos]:
            print(f"Swapping :: {start_pointer} -> {value_at_pos} [{nums[start_pointer]} - {nums[value_at_pos]}]")
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1
    print(f"[sorted array is :: {nums}]")
    for idx in range(len(nums)):
        if nums[idx] != idx + 1:
            return idx+1
    
    return total_len + 1

items = [-3, 1, 5, 4, 2]
res = find_first_missing_positive_number(nums=items)
print(f"The first missing number is :: {res}")
