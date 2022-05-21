"""
Problem Statement
Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the input array.
Note that the function should return duplicate integers if necessary;
 for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
"""

def find_three_largest_numbers(arr):
    """
    Time: O(N)
    Space: O(1)
    """
    largest_triplet = [float('-inf'), float('-inf'), float('-inf')]
    for elem in arr:
        update_largest(largest_triplet, elem)
    return largest_triplet

def update_largest(largest_triplet, elem):
    if elem > largest_triplet[2]:
        shift_number(largest_triplet, elem, 2)
        pass
    elif elem > largest_triplet[1]:
        shift_number(largest_triplet, elem, 1)
        pass
    elif elem > largest_triplet[0]:
        shift_number(largest_triplet, elem, 0)
        pass

def shift_number(sub_array, num, idx):
    for i in range(idx+1):
        if i == idx:
            sub_array[i] = num
        else:
            sub_array[i] = sub_array[i+1]

if __name__ == "__main__":
    a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    res = find_three_largest_numbers(arr=a)
    print(f"[main] the three largest numbers are :: {res}")