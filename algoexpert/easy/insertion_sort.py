"""
Insertion Sort
Problem Statement
Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Insertion Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3] 
Sample output: [2, 3, 5, 5, 6, 8, 9]

"""

def insertion_sort(arr):
    """
    Time:
    worst/avg: O(N^2)
    Space: O(1)
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] > arr[j-1]:
                break
            # swap, since the previous number is lesser than the current j number
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

if __name__ == "__main__":
    arr = [8, 5, 2, 9, 5, 6, 3]
    arr = insertion_sort(arr)
    print(f"The array is sorted via insertion sort ::: {arr}")
