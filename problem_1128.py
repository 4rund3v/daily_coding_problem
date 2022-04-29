"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3],
 return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def permutate(source):
    """
    Given an array of integers, find all the possible permutations.
    """
    permutations = []
    def helper(index, source):
        if index == len(source)-1:
            permutations.append(source[:])
        else:
           for pos in range(index, len(source)):
                source[index], source[pos] = source[pos], source[index]
                helper(index+1, source)
                source[index], source[pos] = source[pos], source[index]
    helper(0, source)
    return permutations

if __name__ == "__main__":
    source = [1 , 2 , 3]
    permutations = permutate(source)
    print(f"[main] the permutations calculated are :: {permutations}")