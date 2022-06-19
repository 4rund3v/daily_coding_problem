"""
Find the First K Missing Positive Numbers (hard) #
Given an unsorted array containing numbers and a number 'k',
 find the first 'k' missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:
Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:
Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""

def first_k_missing_positive_integers(nums):
    # cyclic sort the integers
    # find the numbers that are not in their places
    start_pointer = 0
    total_len = len(nums)
    while start_pointer < total_len:
        value_at_pos = nums[start_pointer] - 1
        if nums[start_pointer] > 0 and nums[start_pointer] <= total_len and nums[start_pointer] != nums[value_at_pos]:
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1
    missing_integers = []
    for idx in range(total_len):
        if nums[idx] != idx +1:
            missing_integers.append(idx+1)
    return missing_integers

items = [3 ,-1, 4, 5, 0, 5, 2, 7]
res = first_k_missing_positive_integers(nums=items)
print(f"Sorted numbers are :::: {items}")
print(f"The first k missing integers is :: {res}")
