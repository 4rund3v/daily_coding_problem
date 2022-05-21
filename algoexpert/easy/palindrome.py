"""
Palindrome Check
Problem Statement
Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is a palindrome. A palindrome is dened as a string that is written the same forward and backward.

Sample input:"abcdcba"

Sample output: True (it is a palindrome)
"""

def check_palindrome(word):
    """
    Pointer approach (Best/Simple)    
    Time: O(N)
    Space: O(1)
    """
    start = 0
    end = len(word) -1
    while end > start:
        if word[start] != word[end]:
            return False
        end -= 1
        start += 1
    return True

def check_palindrome_alt1(word):
    """
    String approach  
    Time: O(N^2) as strings are fixed, each time we append we are recreating the string
    Space: O(N)
    """
    reversed_string = ""
    for i in reversed(range(len(word))):
        # This string addition is an expensive one, rather use list.append and at the end "".join(list)
        reversed_string += word[i]
    return reversed_string == word

def check_palindrome_alt2(word, start=0):
    """
    Recursive approach
    Time: O(N)
    Space: O(N) as the call stacks occupies mem.
    """
    end =  len(word) - 1 - start
    if start >= end:
        return True
    if word[start] != word[end]:
        return False
    return check_palindrome_alt2(word, start+1)
        
    

if __name__ == "__main__":
    test_cases = ["abcdcba", "level", "router", "spider", "radar"]
    for word in test_cases:
        res = check_palindrome(word=word)
        print(f"[main] The word palindrome test returned : [{word}]->[{res}]")

    for word in test_cases:
        res = check_palindrome_alt1(word=word)
        print(f"[main][Alternative]The word palindrome test returned : [{word}]->[{res}]")

    for word in test_cases:
        res = check_palindrome_alt2(word=word)
        print(f"[main][AlternativeRecursive]The word palindrome test returned : [{word}]->[{res}]")
