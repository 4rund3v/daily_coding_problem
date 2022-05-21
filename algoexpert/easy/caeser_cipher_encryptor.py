"""
Caesar Cipher Encryptor
Problem Statement
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".

Sample input:"xyz", 2
Sample output:"zab"
FYI:
   ord(a) = 97
   chr(97) = 'a'

"""

def chiper_encryptor(string, key):
    """
    The chiper encryptor, will shift the character based on the key
    """
    new_letters = []
    # edge case where the key is like 132 ( 26*5 + 2) so we would be moving by 2
    key = key % 26
    # alphabets = list("abcdefghijklmnopqrstuvwxyz")
    # for letter in string:
    #     new_letters.append(get_encrypted_letter(letter, key, alphabet))
    for letter in string:
        new_letters.append(get_encrypted_letter(letter, key))
    return "".join(new_letters)

def get_encrypted_letter(letter, key):
    # new_index = alphabet.index(letter) + key
    # Since length of the array is 25
    # if new_index < 26:
    #     return alphabet[new_index]
    # return chr(-1 + (new_index % 25))
    new_letter_code = ord(letter) + key
    if new_letter_code <= 122:
        return chr(new_letter_code)
    return chr(96+ (new_letter_code% 122))

def decryptor(string, key):
    new_letters = []
    key = key % 26
    for letter in string:
        new_letters.append(get_decrypted_letter(letter, key))
    return "".join(new_letters)

def get_decrypted_letter(letter, key):
    """
    Decrypts the letter back based on the key
    """
    new_letter_code = ord(letter) - key
    if new_letter_code <= 122 and new_letter_code > 96:
        return chr(new_letter_code)
    if new_letter_code <= 96:
        return chr(122-(96-new_letter_code))
    else:
        return chr(96 + (new_letter_code % 122))

if __name__ == "__main__":
    word = "zachooyammet"
    new_word = chiper_encryptor(string=word, key=2)
    print(f"[main] the chiper word is   :: {word} --> {new_word}")

    res = decryptor(new_word, 2)
    print(f"[main] the original word is :: {new_word} --> {res} ")
