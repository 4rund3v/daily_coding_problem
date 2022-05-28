
def longest_non_repeating_char(word):
    """
     Time is : O(n) -> 
     Space is : O(m) -> m unique chars in the word n

    """
    char_map = {}
    max_sub_string = 0
    start_pointer = 0
    for index, char in enumerate(word):
        if char in char_map:
            start_pointer = max(start_pointer , char_map[char]+1)
        sub_string_len = (index - start_pointer ) + 1
        if sub_string_len > max_sub_string:
            max_sub_string = sub_string_len
        char_map[char] = index
    return max_sub_string

if __name__ == "__main__":
    test_cases = (
            "xyzxp",
            "pqbrstburwpvy",
            )
    for test_case in test_cases:
        res = longest_non_repeating_char(word=test_case)
        print(f"[main] The longest non repeating char window is :: {test_case} --> {res}")
