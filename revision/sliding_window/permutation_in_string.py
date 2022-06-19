"""
n! number of permutations
abc ->
   abc
   acb
   bac
   bca
   cab
   cba


Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

"""

def find_permutation(word, pattern):
    perm_exists = False
    char_freq_map = {}
    for char in pattern:
        char_freq_map[char] = char_freq_map.get(char, 0) + 1

    start_pointer = 0
    matched = 0
    for end_pointer in range(len(word)):
        curr_char = word[end_pointer]
        if curr_char in char_freq_map:
            char_freq_map[curr_char] -= 1
            if char_freq_map[curr_char] ==0:
                matched += 1
        if matched == len(char_freq_map):
            return True
        if end_pointer >= len(pattern) - 1:
            char_to_pop = word[start_pointer]
            start_pointer += 1
            if char_to_pop in char_freq_map:
                if char_freq_map[char_to_pop] == 0:
                    matched -= 1
                char_freq_map[char_to_pop] += 1
    return perm_exists

word="aaacb"
pattern = "cab"
res = find_permutation(word, pattern)
print(f"permutation present :: {res}")
