def binary_search(arr, idx):
    """
    Works only when the array is sorted
    T: O(log n)
    S: depth of the tree
    """
    if len(arr) < 1:
        return None

    def helper(arr, start, end, target):
        """
        The recursive approach consumes more space than the iterative approach
        The space is (log n)
        """        
        if start > end:
            return None
        mid = start + (end-start) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return helper(arr, start, end, target)

    idx = helper(arr, 0, len(arr) -1, target)
    return idx


if __name__ == "__main__":
    test_cases = (
            ([], 10),
            ([10], 10),
            ([1, 2,3,4,5,6,7,8,9,10,11,12,13], 4),
            ([11,12,13,14,15,16,17,18,19,20,21, 22, 23], 14),
            )
    for input_array,target in test_cases:
        res = binary_search(input_array, target)
        print(f"[main] The binary search result is :: {input_array}/[{target}] -> {res}\n")
