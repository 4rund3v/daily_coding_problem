"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
# TODO : Handle negative numbers in list
"""

def sub_array_sum(input_array, k):
    start = 0
    end = 1
    current_sum = 0
    for index in range(len(input_array)):
        current_sum += input_array[index]
        while current_sum > k:
            # resize the window
            current_sum -= input_array[start]
            start += 1

        if current_sum == k:
            break
        end += 1
    if current_sum != k:
        return 0,0        
    return start, end

if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5, 6, 7, 11, 8, 77]
    k = 77
    start, end = sub_array_sum(input_array=input_array, k=k)
    print(f"[main] the sub array that contains the sum is [{k}]::: {input_array[start: end]}")