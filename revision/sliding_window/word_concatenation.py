"""
Words Concatenation (hard) #
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""


def find_word_concatenation(word, sub_words):
    if len(sub_words) == 0 or len(sub_words[0])==0:
        return []
    word_frequency = {}
    for word in sub_words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(sub_words)
    word_length = len(sub_words[0])


    for i in range((len(word) - words_count*word_length)+1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j*word_length
            curr_word = word[next_word_index: next_word_index+word_length]
            # since its not overlapping, if not found, break
            if curr_word not in word_frequency:
                break
            
            # in case its found, add to words seen
            if curr_word not in words_seen:
                words_seen[curr_word] = 0
            words_seen[curr_word] += 1
        
            if words_seen[curr_word] > word_frequency[curr_word]:
                break

            if j+1 == words_count:
                result_indices.append(i)        
        pass

    return result_indices