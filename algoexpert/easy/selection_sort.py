"""
Selection Sort
Problem Statement
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3]

Sample output: [2, 3, 5, 5, 6, 8, 9]
"""

def selection_sort(arr):
    """
    @param [] arr: the array to be sorted
    Time:  O(N^2)
    Space: O(1)
    """
    sorted_index = 0
    while sorted_index < len(arr) - 1:
        smallest_index = sorted_index
        for i in range(smallest_index+1, len(arr)):
            if arr[smallest_index] > arr[i]:
                smallest_index = i
        arr[sorted_index], arr[smallest_index] = arr[smallest_index], arr[sorted_index]
        sorted_index += 1
    return arr


if __name__ == "__main__":
    arr = [8, 5, 2, 9, 5, 6, 3]
    selection_sort(arr)
    print(f"[main] The sorted array is :: {arr}")
