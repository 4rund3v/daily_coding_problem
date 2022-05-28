def get_powersets_array(arr):
    """
    The power set has 2^n elements
    """
    power_sets = []
    def helper(arr, idx, sub_set):
        if idx == len(arr):
            power_sets.append(sub_set[:])
            return
        helper(arr, idx+1, sub_set)
        sub_set.append(arr[idx])
        helper(arr, idx+1, sub_set)
        sub_set.pop()
    helper(arr, 0, [])
    return power_sets

if __name__ == '__main__':
    test_cases = (
           [],
           [1],
           [1, 2, 3],
           [1, 8, 7]
           )
    for test_case in test_cases:
        power_set = get_powersets_array(arr=test_case)
        print(f"[main] The power set for test case :[{test_case}] is -> \n{power_set}\n")
