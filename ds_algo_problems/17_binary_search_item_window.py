def binary_search(arr, target):
    """
    Recursive approach takes
     Time : O(log N + log N) -> O(2 log N) -> O(log N)
     Space : log N ( call stacks
    """
    res = [-1, -1]
    if len(arr) < 1:
        return res
    left_extreme = helper_left_extreme(arr, target, start=0, end=len(arr)-1)
    right_extreme = helper_right_extreme(arr, target, start=0, end=len(arr)-1)
    return left_extreme,right_extreme

def helper_left_extreme(arr, target, start, end):
    """
     Find the left extreme occurance of a target value
     Time : Log N
     Space : log N
    """
    if start > end:
        return -1
    mid = start + (end-start) // 2
    if arr[mid] == target:
        if mid == 0:
            return mid
        if arr[mid - 1] != target:
            # left extreme since the mid-1 elem is not target
            return mid
        end = mid - 1
        return helper_left_extreme(arr, target, start, end)

    elif arr[mid] > target:
        end = mid -1
        return helper_left_extreme(arr, target, start, end)
    else:
        start = mid + 1
        return helper_left_extreme(arr, target, start, end)


def helper_right_extreme(arr, target, start, end):
    """
     Find the right extreme occurance of a target value
     Time : Log N
     Space : log N
    """
    if start > end:
        return -1
    mid = start + (end-start) // 2
    if arr[mid] == target:
        if mid == len(arr) -1:
            return mid
        if arr[mid + 1] != target:
            # right extreme since the mid+1 elem is not target
            return mid
        start = mid + 1
        return helper_right_extreme(arr, target, start, end)

    elif arr[mid] > target:
        end = mid -1
        return helper_right_extreme(arr, target, start, end)
    else:
        start = mid + 1
        return helper_right_extreme(arr, target, start, end)
    

if __name__ == "__main__":
    test_cases = (
            ([], 10),
            ([10], 10),
            ([11], 10),
            ([1, 2, 3, 4, 5, 5,5, 5, 5, 6,7,8,8,8,8,8,9], 5),
            ([1, 2, 3, 4, 5, 5,5, 5, 5, 6,7,8,8,8,8,8,9], 8),
            ([1, 2, 3, 4, 5, 5,5, 5, 5, 6,7,8,8,8,8,8,9], 7),
            ([1, 2, 3,3,3,3, 4, 5, 5, 5, 5, 5, 6,7,8,8,8,8,8,9], 3),
            )
    for input_array, target in test_cases:
        res = binary_search(input_array, target)
        print(f"[main] The index of the target in the array is :: {input_array} / [{target}] is --> {res}")
    pass
