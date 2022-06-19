"""
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

"""


def length_of_longest_substring(word, replace_count):
    longest_ones_substring_len = 0
    start_pointer = 0
    char_freq_map = {}
    max_distinct_char_count = 0
    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]
        char_freq_map[curr_char] = char_freq_map.get(curr_char, 0) + 1

        # max distinct char count in the given window
        max_distinct_char_count = max(max_distinct_char_count, char_freq_map[curr_char])
        # check if the window is valid
        if (end_pointer - start_pointer + 1) - max_distinct_char_count > replace_count:
            char_to_pop = word[start_pointer]
            char_freq_map[char_to_pop] -= 1
            start_pointer += 1
        
        longest_ones_substring_len = max(longest_ones_substring_len, end_pointer - start_pointer + 1)
    return longest_ones_substring_len

word = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
replace_count = 3
res = length_of_longest_substring(word, replace_count)
print(res)