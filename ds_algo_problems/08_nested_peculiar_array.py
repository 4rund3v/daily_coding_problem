


def find_array_power_sum(arr, depth=1):
    """
    The complexity is
    Time : O(N) ( total number of elements, in array and subarrays
    Space : O(d) the maximum depth of the call stack
               
    """
    local_sum = 0
    for elem in arr:
        print(f"[find_array_power_sum] The elem is :: {elem}")
        if type(elem) is list:
            local_sum += find_array_power_sum(elem, depth=depth+1)
        else:
            local_sum += elem
    return local_sum ** depth


if __name__ == "__main__":
    test_cases = (
            [],
            [1, 2, [3,4], [[2]]],
            )
    for test_case in test_cases:
        res = find_array_power_sum(arr=test_case)
        print(f"[main] The array powered sum is :: {test_case} -> {res}")
