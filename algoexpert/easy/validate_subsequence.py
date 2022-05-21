"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.
  
  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4]  form a subsequence of the array
  [1, 2, 3, 4] , and so do the numbers .
 Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

  Sample Input array = [5, 1, 22, 25, 6, -1, 8, 10]
  sequence  = [1, 6, -1, 10]
  Sample Output true
"""


def valid_subsequence(complete_array, sub_array):
    """
    Find if the provided sub array is a contained in the complete array
    :@param [] complete_array: The complete sequence
    :@param [] sub_array: The sub sequence being checked
    return bool : Indicating if the subseuqnce is valid or not
    : O(n) Time, no space O (1)
    """
    if len(complete_array) < len(sub_array) or not sub_array:
        print(f"[valid_subsequence] The input validation failed.")
        return False
    main_pointer = 0
    sub_pointer = 0
    while main_pointer < len(complete_array) and sub_pointer < len(sub_array):
        if complete_array[main_pointer] == sub_array[sub_pointer]:
            sub_pointer += 1
        main_pointer += 1
    return sub_pointer == len(sub_array)

if __name__ == "__main__":
    a =  [5, 1, 22, 25, 6, -1, 8, 10]
    b = [1, 6, -1, 10]
    res = valid_subsequence(a, b)
    print(f"[main] The result is :: {res}")