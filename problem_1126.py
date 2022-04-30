"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""


def minimum_sqaures_count(num):
    half_way = int( num ** 0.5 )
    squares = [ i*i for i in range(1, half_way+1)]

    """
    squares = [1, 4, 9, 16] 
    minimum_squares_required = { 1: 1,
                                 2:2,
                                 3:3,
                                 4:1,
                                 5: 2 ( 2^2 , 1),
                                 ....
                                 19: (??) ( worse case scenario : 19)
    }
    """
    minimum_squares_required = [i for i in range(0, num+1)]
    print(f"[minimum_sqaures_count] the minimum squares required is :: {minimum_squares_required}")
    for index in range(2, num+1):
        squares_required = [ minimum_squares_required[index - perfect_square] + 1  for perfect_square in squares if (index - perfect_square) >= 0]
        print(f"[minimum_sqaures_count] the index and the squares for that are [{index}]:: {squares_required}")
        minimum_squares_required[index] = min(squares_required)
    return minimum_squares_required[num]

if __name__ == "__main__":
    num = 24
    minimum_squares_required = minimum_sqaures_count(num)
    print(f"the minimum squares required to get [{num}]:::{minimum_squares_required}")