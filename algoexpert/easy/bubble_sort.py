"""
Bubble Sort

Problem Statement
Write a function that takes in an array of integers and returns a sorted version of that array.
Use the Bubble Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3] Sample output: [2, 3, 5, 5, 6, 8, 9]

*** USE WHEN NO EXTRA SPACE IS REQUIRED ***
"""

def bubble_sort(arr):
    """
    In each iteration, the numbers are going to be sorted in the exact position
    Time Complexity : O(N^2)
                     best case when the array is sorted : O(N)
    Space complexity : O(1)
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        counter = 0
        for i in range(len(arr)-1-counter):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted= False
        counter += 1
        print(f"[bubble_sort] The arr is : {arr}")
    return arr

if __name__ == "__main__":
    arr = [8, 5, 2, 9, 5, 6, 3]
    arr = bubble_sort(arr)
    print(f"[main] The sorted array is ::: {arr}")
