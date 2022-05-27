

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr, k):
    rotation_factor = k or k % len(arr) 
    if not arr or len(arr) == 1 or rotated_arr == 0:
        return arr
    '''
    Brute force :
       copy the k elements into an another arr
       then swap each element by k pos, 
       then fill in the first k elements with those in the rotated arr 
       This will be O(n) time and O(~k) space
    Alternative
       First reverse the elements start to end
       Then re reverse the two parts ( first k places, remaining n-k places)
    '''
    print(f"[rotate_array] The reversal begins  ")
    reverse(arr, start=0, end=len(arr) - 1)
    print(f"[rotate_array] The reversal gives -> {arr}  ")
    reverse(arr, start=0, end=rotate_factor-1)
    print(f"[rotate_array] The reversal gives -> {arr}  ")
    reverse(arr, start=rotate_factor, end=len(arr)-1)
    print(f"[rotate_array] The reversal gives -> {arr}  ")
    return arr


if __name__ == "__main__":
    test_cases = (
            ([], 3),
            ([1,2,3], 2),
            ([-4, 6, -6],1),
            )
    for input_arr, rotate_factor in test_cases:
        rotated_arr = rotate_array(arr=input_arr.copy(), k=rotate_factor)
        print(f"[main] The input array and the rotated array are w.r.t. factor : {input_arr} -> {rotate_factor},{rotated_arr}")
