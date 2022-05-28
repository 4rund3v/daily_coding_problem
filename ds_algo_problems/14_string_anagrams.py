def group_anagrams(string_list):
    # Time s * nlogn
    # Space is also s * n
    sorted_char_map = {}
    for word in string_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in sorted_char_map:
            sorted_char_map[sorted_word] = []
        sorted_char_map[sorted_word].append(word)
    return sorted_char_map.values()


if __name__ == "__main__":
    test_cases = (
             [],
             [''],
             ["abc", "cab", "star", "rats", "pan", "nap"],
             ["xmas", "maxs", "tab", "bat", "abt"]
            )
    for test_case in test_cases:
        anagrams = group_anagrams(test_case)
        print(f"[main] The test case and the anagrams are :: {test_case} -> {anagrams}\n")
