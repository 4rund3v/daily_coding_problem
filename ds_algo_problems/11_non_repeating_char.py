
def first_non_repeating_char_index(word):
    """
    Time is O(n) -> O(n+n) -> O(2n) -> O(n)
    Space is O(1) since the characters are lowercase, upercase and numbers
                                             26, 26, 10 => 62 O(62) = O(1)
    """
    visited_chars = {}
    for char in word:
        if char not in visited_chars:
            visited_chars[char] = 0
        visited_chars[char] += 1
    for i in range(0, len(word)):
        if visited_chars[word[i]] == 1:
            return i
    return None


if __name__ == "__main__":
    test_cases = (
            "abcAAbbab",
            "aabbcc",
            "abcDcba"
            )
    for test_case in test_cases:
        idx = first_non_repeating_char_index(word=test_case)
        print(f"[main] The first char that is non repeating for {test_case} is {idx}")
