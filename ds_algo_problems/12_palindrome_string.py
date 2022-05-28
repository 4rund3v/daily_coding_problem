
def is_palindrome(word):
    """
    Time is O(n)
    Space is O(1)
    """
    if not word:
        return False
    if len(word) == 1:
        return True
    left_pointer = 0
    right_pointer = len(word) -1
    while left_pointer < right_pointer:
        if word[left_pointer] != word[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True

if __name__ == "__main__":
    test_cases = (
            "malayalam",
            "doom",
            "rotor",
            "dragon",
            "radar",
            )
    for test_case in test_cases:
        res = is_palindrome(word=test_case)
        print(f"[main] The word :{test_case} palindrom->{res}")
