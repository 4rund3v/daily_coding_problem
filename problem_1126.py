"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""


def minimum_sqaures_count(num):
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
    half_way = int( num ** 0.5 )
    squares = [ i*i for i in range(1, half_way+1)]
    minimum_squares_required = [i for i in range(0, num+1)]
    for index in range(2, num+1):
        minimum_squares_required[index] = min([ minimum_squares_required[index - perfect_square] + 1  for perfect_square in squares if (index - perfect_square) >= 0])
    return minimum_squares_required[num]

if __name__ == "__main__":
    num = 24
    minimum_squares_required = minimum_sqaures_count(num)
    print(f"[main] the minimum squares required to get [{num}]::: {minimum_squares_required}")