"""
Longest Substring with Same Letters after Replacement 
Problem Statement #
Given a string with lowercase letters only,
 if you are allowed to replace no more than 'k' letters with any letter,
  find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def length_of_longest_substring(word, replace_count):
    longest_substring_len = 0
    char_frequency_map = {}
    start_pointer = 0
    max_repeating_char_count = 0
    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]
        char_frequency_map[curr_char] = char_frequency_map.get( curr_char, 0) + 1
        
        # find the maximum repeating char
        max_repeating_char_count = max(max_repeating_char_count, char_frequency_map[curr_char])
        
        # if the current window contains more char than the max repeating char, shrink the window
        window_len = end_pointer - start_pointer + 1
        if ((window_len) - max_repeating_char_count ) > replace_count:
            char_to_pop = word[start_pointer]
            char_frequency_map[char_to_pop] -= 1
            start_pointer += 1
        longest_substring_len = max(longest_substring_len, window_len)
    return longest_substring_len

word = "abbcb"
replace_count = 1
res = length_of_longest_substring(word, replace_count)
print(f"The length of the longeset substring is :: {res}")
