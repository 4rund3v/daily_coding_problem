def array_permutations(arr):
    """
    for an array of 3 items
        _ _ _
        3 2 1 ways to fill each positions
        The n! ways to fill this, 
        i.e the total number of permutations is n!

    Space: O(n! * n) -> n calls on the stack and the n! number of storing
    Time: O(n! * n)
    """
    permutations = []
    def helper(arr, idx):
        if idx == len(arr) -1:
            # this is a O(n) operation, that occurs in n!
            permutations.append(arr[:])
            return
        for j in range(idx, len(arr)):
            swap(arr, idx, j)
            helper(arr, idx+1)
            swap(arr, idx, j)
        # print(f"[helper] The arr after one complete recursion tree is : {arr}")
    helper(arr, 0)
    return permutations

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    test_cases = ([1,2,3], [12, 43, 22, -1])
    for test_case in test_cases:
        permutations = array_permutations(arr=test_case)
        print(f"[main] The permutations for {test_case} is {permutations}")
