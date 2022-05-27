
def fibbonacci_numbers(n, cache):
    """
        f(5)
        /  \
    f(4)    f(3)
    / \      / \
f(3) f(2)   f(2) f(1)       
   T: O(2^n)
   since every step we are doing 2^x steps

   with the memoization, the Time Complexity is O(n)
                         since no extra calculations are made
   Space is O(n)
    """
    if n <=0:
        return 0
    if n == 1:
        return 1
    if n-1 not in cache:
        cache[n-1] =  fibbonacci_numbers(n-1, cache)
    if n-2 not in cache:
        cache[n-2] = fibbonacci_numbers(n-2, cache)
    return cache[n-1] + cache[n-2]

def alt_fibbonacci(n):
    """
     Iteratively approach
      Time : O(n)
      Space : O(1)
    """
    prev = 0
    curr = 1
    for i in range(2, n+1):
        present = curr + prev 
        prev, curr = curr, present
    return curr

if __name__ == "__main__": 
     test_cases = [2, 10, 6, 123, 398, 399, 400, 401]
     for test_case in test_cases:
         cache = {}
         # res = fibbonacci_numbers(test_case, cache={})
         res = alt_fibbonacci(test_case)
         print(f" The fibonnaci number at pos : {test_case} is ---> {res}")

