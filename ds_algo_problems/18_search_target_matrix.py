
def binary_search_matrix(input_matrix, target):
    """
    Iterative approach
    m is the number of rows
    n is the number of columns
    Time : O ( log m + log n)
    Space : O(1)
    """
    # find the matching row
    # Then binary search the row for the target
    row_count = len(input_matrix) - 1
    col_count = len(input_matrix[0]) - 1
    print(f"[binary_search_matrix] The row count and the col count is :: {row_count}, {col_count}") 
    row_index = -1
    floor = 0
    top = row_count
    while floor <= top:
        mid = floor + (top-floor)// 2
        selected_row = input_matrix[mid]
        # print(f"[binary_search_matrix] The selected row is :: {selected_row} target[{target}]")
        if selected_row[0] > target:
            top = mid - 1
        elif selected_row[-1] < target:
            floor = mid + 1
        else:
            # case where the target lies within the selected row
            row_index = mid
            break
    print(f"[binary_search_matrix] The row index selected is :: {row_index} -> {input_matrix[row_index]}")
    if row_index == -1:
        return -1, -1

    col_index = -1
    start = 0
    end = col_count
    row = input_matrix[row_index]
    while start <= end:
        mid = start + (end-start)//2
        if row[mid] == target:
            col_index = mid
            break
        if row[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return row_index, col_index



if __name__ == "__main__":
    test_cases = (
            ([ [1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
            ([ [1, 2, 3], [4, 5, 6], [7, 8, 9]], 7),
            ([ [1, 2, 3], [4, 5, 6], [7, 8, 9]], 4),
            ([ [1, 2, 3], [4, 5, 6], [7, 8, 9]], 11),
            ([ [1, 2, 3], [4, 5, 6], [7, 8, 9]], -2),
            )
    for input_matrix, target in test_cases:
        res = binary_search_matrix(input_matrix, target)
        print(f"[main] The res for the input array is :: {input_matrix}/{target} -> {res}")
