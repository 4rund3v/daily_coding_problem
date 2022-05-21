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
    
if __name__ == "__main__":
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    ts = 10
    res = two_number_sum(a, ts)
    print(f"main: The res is :: {res}")
    
