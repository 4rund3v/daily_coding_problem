"""
Smallest Window containing Substring (hard) #
Given a string and a pattern,
 find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""


def smallest_subarray_containg_pattern(word, pattern):
    subarray_len = 0
    char_freq_map = {}
    for char in pattern:
        char_freq_map[char] = char_freq_map.get(char, 0) + 1
    

    start_pointer = 0
    substring_start = 0
    matched = 0
    min_length = len(word) + 1

    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]

        if curr_char in char_freq_map:
            char_freq_map[curr_char] -= 1
            if char_freq_map[curr_char] >= 0:
                matched += 1
            
        # shrink the window
        while matched == len(pattern):
            if min_length > (end_pointer-start_pointer+1):
                min_length = end_pointer-start_pointer+1
                substring_start = start_pointer
            
            char_to_pop = word[start_pointer]
            start_pointer += 1
            if char_to_pop in char_freq_map:
                if char_freq_map[char_to_pop]==0:
                    matched -= 1
                char_freq_map[char_to_pop] += 1
    if min_length > len(word):
        return ""
    return word[substring_start:substring_start+min_length]

word = "aabdec"
pattern = "abc"
res = smallest_subarray_containg_pattern(word, pattern)
print(f"the smallest subarray containg pattern is ::: {res}")
