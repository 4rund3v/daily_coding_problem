"""
Find the Corrupt Pair (easy) #
We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'.
 The array originally contained all the numbers from 1 to 'n', but due to a data error,
  one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""

def corrupt_pair(nums):
    # cyclic sort the elements in place 
    # then iterate through the elemtns and find the first item that doesnot match the index
    # the matching number and its index is the corrupt pair
    start_pointer = 0
    while start_pointer < len(nums):
        value_at_pos  = nums[start_pointer] - 1
        if nums[start_pointer] != nums[value_at_pos]:
            nums[start_pointer], nums[value_at_pos] = nums[value_at_pos], nums[start_pointer]
        else:
            start_pointer += 1

    for idx in range(len(nums)):
        if nums[idx]  != idx +1:
            print(f"duplicate is :: {nums[idx]} @ missing is {idx+1}")
            return [nums[idx], idx+1]

    return []

items = [3, 1, 2, 3, 6, 4]
res = corrupt_pair(items)
print(f" the res :: {res}")
