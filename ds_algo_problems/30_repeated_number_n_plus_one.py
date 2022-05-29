"""
given an array that has n+1 integers, where there is exactly one number is repeated.
the range of numbers is [1 to n] inclusive
n =      [1, 2, 5, 3, 4, 5] 
index =   0  1  2  3  4  5

exactly one number is repeated., indicates a cycle
"""

def find_duplicate(nums):
    """
    Floyd's hare and tortoise algo,
    Time : O(n)
    Space : O(1)
    """
    hare = tortoise = 0
    while hare != None:
        tortoise = nums[nums[tortoise]]
        hare = nums[nums[nums[hare]]]
        if tortoise == hare:
            break
    print(f"[find_duplicate] The hare and tortoise is at :: {hare} -> {tortoise}")
    if hare != tortoise:
        return None
    index = 0
    while nums[index] != tortoise:
        index = nums[index]
        tortoise = nums[tortoise]
        pass
    print(f"[find_duplicate] The duplicate num [{tortoise}] is and at index :: {index}")
    return tortoise
    

if __name__ == "__main__":
    nums = [  1, 4, 5, 3, 2, 5]
    duplicate_val = find_duplicate(nums)
    print(f"[main] The duplicate is at : {nums} -> {duplicate_val}")