"""
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def non_repeat_substring(word):
    start_pointer = 0
    max_distinct_char_substring_len = 0
    distinct_char_set = set()
    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]
        print(f"New Char :: {curr_char}")
        while curr_char in distinct_char_set:
            char_to_pop = word[start_pointer]
            print(f"poppping :: {char_to_pop}")
            distinct_char_set.remove(char_to_pop)
            start_pointer += 1
        print(f"adding :: {curr_char}")
        distinct_char_set.add(curr_char)
        curr_len = end_pointer - start_pointer  + 1
        max_distinct_char_substring_len = max(curr_len, max_distinct_char_substring_len)
    return max_distinct_char_substring_len

word = "abccde"
res = non_repeat_substring(word=word)
print(f"The longest non repeating substring is :: {res}")
