"""
Nth Fibonacci
Problem Statement
The Fibonacci sequence is dened as follows: 
the first number of the sequence is 0,
the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.

Sample input: 6

Sample output: 5 (0, 1, 1, 2, 3, 5)
"""

def find_fibbonacci(n):
    """
    Time Complexity of ( O(2^ n)) as each branch we are doing it two times
    Space complexity of ( O(n) as at any time in the memory,  we would be storing at max n frames on the call stack)
    """
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return find_fibbonacci(n-1) + find_fibbonacci(n-2)

def find_fibbonacci_alt(n, memoize):
    """
    Time Complexity of ( O(n)) as each branch we are doing it two times
    Space complexity of ( O(n) as at any time in the memory,  we would be storing at max n frames on the call stack)
    """
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = find_fibbonacci_alt(n=n-1, memoize=memoize) + find_fibbonacci_alt(n=n-2, memoize=memoize)
        return memoize[n]

def find_fibbonacci_alt_2(n):
    """
    Time Complexity of ( O(n)) as each branch we are doing it two times
    Space complexity of ( O(1) space)
    """
    last_two = [0, 1]
    counter = 3 
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0], last_two[1] = last_two[1], next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]

if __name__ == "__main__":
    res = find_fibbonacci(6)
    print(f"[main] the res is :: {res}")
    
    res = find_fibbonacci_alt(6, {1:0, 2:1})
    print(f"[main] the res alt is :: {res}")
    res = find_fibbonacci_alt_2(6)
    print(f"[main] the res alt is :: {res}")
    pass