'''
def sorted_squares(arr):
    """
    Brute force -> O(n) -> sorted_arr = [i*i for i in arr]
                   O(nlogn) -> sorted_arr.sort() # tims sort
    """
    sorted_arr = [i*i for i in arr]
    sorted_arr.sort()
    return sorted_arr
Since the arr is on a umber line the squares are equally away from the origin
'''
def sorted_squares(arr):
    '''
    Using the concept that the val^2 is away from the origin equally
    O(n) since we are traversing the array only once
    '''
    if not arr:
        return arr

    n = len(arr) - 1
    left_index = 0
    right_index = n
    sorted_arr = [0] * (n+1)

    while n >= 0:
        print(left_index , right_index)
        left_square = arr[left_index] ** 2
        right_square = arr[right_index] ** 2
        if left_square > right_square:
            sorted_arr[n] = left_square
            left_index += 1
        else:
            sorted_arr[n] = right_square
            right_index -= 1
        n -= 1
    return sorted_arr


if __name__ == "__main__":
    test_case_inputs = (
            [],
            [1, 3, 5],
            [0, 5, 6, 9 ],
            [-4, -2, 0, 1, 4]
            )
    for test_input in test_case_inputs:
        res = sorted_squares(arr=test_input)
        print(f"[main] The squared sorted arr is inp:[{test_input}]:: {res}")
