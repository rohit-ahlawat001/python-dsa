# Python List and hashmap problems

# Problem Three: Valid Anagram - Check whether two strings have the same character frequencies.


def is_anagram(first_string, second_string):
    # If the strings do not have the same length, they cannot be anagrams.
    if len(first_string) != len(second_string):
    