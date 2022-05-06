"""
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

"""

def contains_triplet(source_numbers):
    source_numbers = [i*i for i in source_numbers]
    # sort the squared numbers
    source_numbers.sort()
    # [(a) 1, 9, 16,25,(b) 36, (c)81]
    # [(a) 1, 9, 16,(b)25,(c)36, 81]
    for c in range(len(source_numbers)-1, 1, -1):
        a = 0
        b = c - 1
        while ( a < b ):
            current_sum = source_numbers[a] + source_numbers[b]
            print(f"[contains_triplet] the iteration is at [{a, b, c}]")
            if ( current_sum == source_numbers[c]):
                print(f"[contains_triplet] The pythogorean triplet found: {(source_numbers[a], source_numbers[b], source_numbers[c])}")
                return True
            elif (current_sum < source_numbers[c]):
                a += 1
            else:
                # (current_sum > source_numbers[c]):
                b -= 1
    return False

if __name__ == "__main__":
    source_num = [2,8,4,6,7,12,8,11,23,56,5,13]
    res = contains_triplet(source_num)
    print(f"[main] the triplet check returned :: {res}")









