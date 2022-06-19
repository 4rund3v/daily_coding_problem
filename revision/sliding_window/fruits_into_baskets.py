"""
Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fill_fruit_baskets(trees, basket_count=2):
    max_fruits_picked = 0
    distinct_fruit_map = {}
    start_pointer = 0
    current_fruit_count = 0
    for end_pointer in range(len(trees)):
        curr_fruit = trees[end_pointer]
        if len(distinct_fruit_map) <= basket_count:
            distinct_fruit_map[curr_fruit] = distinct_fruit_map.get(curr_fruit, 0) + 1
            current_fruit_count += 1
        else:
            while len(distinct_fruit_map) > basket_count:
                tree_to_skip = trees[start_pointer]
                distinct_fruit_map[tree_to_skip] -= 1
                if distinct_fruit_map[tree_to_skip] == 0:
                    del distinct_fruit_map[tree_to_skip]
                start_pointer += 1
                current_fruit_count -= 1
        max_fruits_picked = max(current_fruit_count, max_fruits_picked)
    print(f"start_pointer :: {start_pointer}")
    return max_fruits_picked


trees = ['A', 'B', 'C', 'B', 'B', 'C']
fruit_count = fill_fruit_baskets(trees=trees)
print(f"The max number of fruits that can be picked is :: {fruit_count}")
