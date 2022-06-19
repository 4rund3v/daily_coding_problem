"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Let’s understand this problem with a real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""

def find_subarray_averages(nums, k):    
    averages = []
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        if i >= k - 1:
            averages.append(running_sum / k)
            running_sum -= nums[i-(k-1)]
    return averages

items = [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(items)
res = find_subarray_averages(items, k=5)
print(f"The average subarray is :: {res}")