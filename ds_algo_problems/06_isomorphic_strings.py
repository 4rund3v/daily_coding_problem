
def is_isomorphic(first_word, second_word):
    
    if not first_word or len(first_word) != len(second_word):
        return False


    """
    Since its mentioned that the number of characters are 128 in ascii, the space complexity is O(1)
    Time Comp : T- O(n)
    """
    first_hash = {}
    second_hash = {}
    for i in range(len(first_word)):
        first_char = first_word[i]
        second_char = second_word[i]
        if first_char not in first_hash:
            first_hash[first_char] = second_char
        if second_char not in second_hash:
            second_hash[second_char] = first_char
        if first_hash[first_char] != second_char or second_hash[second_char] != first_char:
            return False
    return True

if __name__ == "__main__":
    test_cases = (
            ("", ""),
            ("abc", "pq"),
            ("abc", "pqr"),
            ("abcd", "pqrq"),
            ("green", "abccd")
            )
    for first_word, second_word in test_cases:
        res = is_isomorphic(first_word, second_word)
        print(f"[main] The isomorphic test for words [{first_word} , {second_word}] is -> {res} ")

