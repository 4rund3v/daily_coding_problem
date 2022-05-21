"""
Product Sum
Problem Statement
Write a function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements,
where "special" arrays inside it should be summed themselves and then multiplied by their level of depth.
 For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample output: 12
 (5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
"""

def product_sum(arr, depth_multiplier):
    """
    :@param [] arr
    :@param int depth_multiplier : Indicates the muliplier
    Space: O(N) ( all items, including the items in the nested array)
    Time : O(d) ( The depth of the array, since the recusion stack max will be the depth of the array)
    """
    current_sum = 0
    for elem in arr:
        if type(elem) is list:
            current_sum += product_sum(arr=elem, depth_multiplier= depth_multiplier+1)
        else:
            current_sum += elem
    return depth_multiplier * current_sum


if __name__ == "__main__":
    a = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    total_sum = product_sum(arr=a, depth_multiplier=1)
    print(f"[main] The product sum calculated is :: {total_sum}")