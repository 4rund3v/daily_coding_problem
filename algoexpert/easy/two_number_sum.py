"""
Problem Statement
Write a function that takes in a non-empty array of distinct integers
and an integer representing a target sum.
 If any two numbers in the input array sum up to the target sum,
  the function should return them in an array, in sorted order.
If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 
Sample output: [-1, 11]

Explanation
We can use a Stack here
"""

def two_number_sum(input_array, target_sum):
    """
    Finds the target sum as the combination 
    of the two numbers from the provided input array
    :@param [] input_array: the provided input array
    :@param int target_sum : the required target sum
    return: []: containing two numbers that sum up to the target_sum if found
              : returns empty when no solution is found

    Runs at O(n)time and O(n)space ( for the number store)
    """
    res = []
    if len(input_array) < 2 or target_sum is None or type(target_sum) is not int:
        print(f"[two_number_sum] The input validation failed. {type(target_sum)}")
        return res
    number_store = set()
    for num in input_array:
        current_difference = target_sum - num
        if current_difference in number_store:
            return [num, current_difference]
        else:
            number_store.add(num)
    return res

def two_number_sum_alt(input_array, target_sum):
    """
    Finds the target sum as the combination 
    of the two numbers from the provided input array
    :@param [] input_array: the provided input array
    :@param int target_sum : the required target sum
    return: []: containing two numbers that sum up to the target_sum if found
              : returns empty when no solution is found

    Runs at O(n^2)time
    """
    res = []
    if len(input_array) < 2 or target_sum is None or type(target_sum) is not int:
        print(f"[two_number_sum] The input validation failed. {type(target_sum)}")
        return res
    
    for index in range(len(input_array)-1):
        first_num = input_array[index]
        for j in range(index, len(input_array)):
            second_num = input_array[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return res

def two_number_sum_alt_2(input_array, target_sum):
    """
    Finds the target sum as the combination 
    of the two numbers from the provided input array
    :@param [] input_array: the provided input array
    :@param int target_sum : the required target sum
    return: []: containing two numbers that sum up to the target_sum if found
              : returns empty when no solution is found

    Runs at O(nlgn)time constant space
    """
    res = []
    if len(input_array) < 2 or target_sum is None or type(target_sum) is not int:
        print(f"[two_number_sum] The input validation failed. {type(target_sum)}")
        return res
    # first sort the array
    input_array.sort()
    left = 0
    right = len(input_array) - 1
    while left < right:
        left_val = input_array[left]
        right_val = input_array[right]
        current_sum = left_val + right_val
        if  current_sum == target_sum:
            return [left_val, right_val]
        elif current_sum > target_sum:
            right -= 1
        elif current_sum < target_sum:
            left += 1            
    return res

if __name__ == "__main__":
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    ts = 10
    res = two_number_sum(a, ts)
    print(f"main: The res of sol1 is :: {res}")
    
    res2 = two_number_sum_alt(a, ts)
    print(f"main: The res of sol2 is :: {res}")

    res2 = two_number_sum_alt_2(a, ts)
    print(f"main: The res of sol3 is :: {res}")