"""
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""

def find_smallest_subarray_with_target_sum(nums, target):

    subarray_sum = 0
    subarray_length = float("inf")
    start_pointer = 0
    
    running_sum = 0
    for end_pointer in range(len(nums)):
        running_sum += nums[end_pointer]
        while running_sum >= target:
            curr_length = end_pointer - start_pointer + 1
            subarray_length = min(curr_length, subarray_length)
            running_sum -= nums[start_pointer]
            start_pointer += 1
    return subarray_length


items = [2, 1, 5, 2, 3, 2]
target = 7
res = find_smallest_subarray_with_target_sum(nums=items, target=target)
print(f"the smallest window is :: {res}")