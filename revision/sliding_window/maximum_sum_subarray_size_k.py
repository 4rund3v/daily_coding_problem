"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""
def find_max_sum_subarray(nums, k):
    max_sum = 0
    window_sum = 0
    start_pointer = 0
    end_pointer = 0
    for end_pointer in range(len(nums)):
        window_sum += nums[end_pointer]
        if end_pointer-start_pointer >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= nums[start_pointer]
            start_pointer += 1
    return max_sum

items = [2, 1, 5, 1, 3, 2]
k = 3
res = find_max_sum_subarray(nums=items, k=3)
print(f"The maximum subarray sum is :: {res}")