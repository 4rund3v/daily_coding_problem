def calculate_max_area_contained(height_arr):
    """
    can y axis be used ?
    does the line in between affect the area?
    thickness of the line ?
    """
    if len(height_arr) <= 1:
        return 0
    """
    # Brute force method
    # The time is O(n^2) and space is O(1)
    max_area = 0
    l = r = w = 0
    i = 0
    while i < len(height_arr) - 1:
        width = 1
        left_wall = height_arr[i]
        for idx in range(i+1, len(height_arr)):
            # print(f"[calculate_max_area_contained] The i and j are :: {left_wall} -> {height_arr[idx]}")
            area = min(left_wall, height_arr[idx]) * width
            if area > max_area:
                max_area = area
                l = left_wall
                r = height_arr[idx]
                w = width
            width += 1
        i+= 1
    """
    # 2 pointer approach
    # O(n) time bound
    # O(1) space bound
    left_pointer = 0
    right_pointer = len(height_arr) - 1
    max_area = 0
    l = r = w = 0
    while left_pointer < right_pointer:
        length = min(height_arr[left_pointer] ,  height_arr[right_pointer])
        width = right_pointer - left_pointer
        area = length * width
        if area > max_area:
            max_area = area
            l = height_arr[left_pointer]
            r = height_arr[right_pointer]
            w = width
        if height_arr[left_pointer] < height_arr[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_area, l, r, w


if __name__ == "__main__":
    test_cases = ( 
            [], 
            [1, 5, 6, 3, 4],
            [3, 7, 5, 6, 8, 4],
            [9, 1, 2, 3, 10]
            )
    for height_arr in test_cases:
        max_area = calculate_max_area_contained(height_arr = height_arr)
        print(f"[main] The area calculated for the heights is :: {height_arr} --> {max_area}")
