"""
Given a string, find the length of the smallest window that contains every distinct character.
 Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

def smallest_distinct_substring(source_string):
    """
    Constraints on sub_string
      -> Must contain all distinct characters from the source.
      -> Can contain duplicates.
      -> Must be smallest such window.
    """
    character_count_map = {i: 0 for i in str(source_string).lower() }
    # print(f"[smallest_distinct_substring]  the char map is : {character_count_map}")
    # {'j': 0, 'i': 0, 'u': 0, 't': 0, 's': 0}
    total_distinct_character_count = len(character_count_map)
    # Represents the distinct character count in the window currently
    distinct_character_count = 0
    start = 0
    minimum_window_length = total_distinct_character_count + 1
    # || j -> i ->  u ->  j ->  i -> t | -> s || u
    # dcc = 3
    # when t is included -> dcc = 4
    # when s is included -> dcc = 5
     # || j -> i ->  u ->  j ->  i -> t  -> s || u
     # {'j': 2, 'i': 2, 'u': 1, 't': 1, 's': 1}
     # while loop :#  j ->|| i ->  u ->  j ->  i -> t  -> s || u start = 1
                   # {'j': 1, 'i': 2, 'u': 1, 't': 1, 's': 1}
                   #  j -> i -> || u ->  j ->  i -> t  -> s || u start = 2
                   # {'j': 1, 'i': 1, 'u': 1, 't': 1, 's': 1}
                   # j -> i -> || u ->  j ->  i -> t  -> s || u start = 2 XXX
    for index in range(len(source_string)):
        char = source_string[index]
        character_count_map[char] += 1

        if character_count_map[char] == 1:
            distinct_character_count += 1
        
        if distinct_character_count == total_distinct_character_count:
            # print(f"[smallest_distinct_substring]  the char map is : {character_count_map}")
            while character_count_map[source_string[start]] > 1:
                character_count_map[source_string[start]] -= 1
                start += 1
            
            window_length = index - start + 1

            if window_length < minimum_window_length:
                minimum_window_length = window_length

            if window_length == total_distinct_character_count:
                break
    
    sub_string = source_string[start: start+minimum_window_length]
    # print(f"[smallest_distinct_substring] The minimum window length is :: {minimum_window_length}")
    # print(f"[smallest_distinct_substring] The smallest window is : [{sub_string}]")
    return len(sub_string)

if __name__ == "__main__":
    minimum_length = smallest_distinct_substring("jiujitsu")
    print(f"[main] The minimum length is :: {minimum_length}")