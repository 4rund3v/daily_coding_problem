def is_monotonic_array(arr):
    '''
    Monotonic is : Either 
       -> Monotonic Incresing   : arr[i] >= arr [i+1]
       -> Monotonic Decresing   : arr[i] <= arr [i+1]

    '''
    if not arr or len(arr) <= 1:
        return True

    monotonic = False
    arr_length = len(arr) - 1
    if arr[0] > arr[arr_length]:
        # non increasing check
        prev_item = arr[0]
        for item in range(1, arr_length+1):
            if arr[item] >= arr[item-1]:
                return monotonic
            prev_item = item
    elif arr[0] < arr[arr_length]:
        # non decreasing check
        prev_item = arr[0]
        for item in range(1, arr_length+1):
            if arr[item] <= arr[item -1]:
                return monotonic
    else:
        # equality check
        for item in range(1, arr_length+1):
            if arr[item] != arr[0]:
                return monotonic
    monotonic = True
    return monotonic

if __name__ == "__main__":
    test_cases = (
            [],
            [1],
            [22,16, 5, 1],
            [-6, -1, 0, 1, 4, 6],
            [3, 4, 5, 6, 7, 10],
            )
    for test_case in test_cases:
        res = is_monotonic_array(arr=test_case)
        print(f"[main] The test case : {test_case} monotonic test -> {res}")
