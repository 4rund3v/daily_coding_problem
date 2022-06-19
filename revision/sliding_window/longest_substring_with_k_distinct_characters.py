"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def longest_substring_with_k_distinct_values(word, k):
    longest_distinct_substring = ""
    longest_len = 0
    start_pointer = 0
    end_pointer = 0
    distinct_char_map = {}
    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]
        distinct_char_map[curr_char] = distinct_char_map.get(curr_char, 0) + 1
        if len(distinct_char_map) <= k:
            curr_len = end_pointer - start_pointer + 1
            longest_len = max(curr_len, longest_len)
        else:
            while len(distinct_char_map) > k:
                char_to_pop = word[start_pointer]
                distinct_char_map[char_to_pop] -= 1
                if distinct_char_map[char_to_pop] == 0:
                    del distinct_char_map[char_to_pop]
                start_pointer += 1
    return longest_len

word = "araaci"
res = longest_substring_with_k_distinct_values(word=word, k=2)
print(res)