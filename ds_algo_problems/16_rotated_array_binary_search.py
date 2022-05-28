
def binary_search_rotated(arr, target):
    """
    Time: O(lgN) each step half of  input is eliminated
    Space: O(lgN) if recursive, O(1) if iterative
    """
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = start + (end-start)// 2
        if arr[mid] == target:
            return mid
        if arr[start] <= arr[mid]:
            # left sub array is sorted
            if arr[mid] > target and arr[start] <= target:
                # explore left
                end = mid - 1
            else:
                # explore right
                start = mid + 1
        else:
            # Right sub array is sorted
            if arr[mid] < target and arr[end] >= target:
                # explore right sub array
                start = mid + 1
            else:
                # explore left sub array
                end = mid - 1
    return - 1


if __name__ == "__main__":
    test_cases = (
            ([], 10),
            ([10], 10),
            ([1, 3, 5, 6, 9, 10, 12, 15, 17], 10),
            ([15, 17, 1, 3, 5, 6, 9, 10, 12], 10),
            )
    for input_array, target in test_cases:
        res = binary_search_rotated(input_array, target)
        print(f"[main] The res index for the target in aray [{input_array}]- {target} is {res}\n")
