# Python List and hashmap problems

# Problem Three: Valid Anagram - Check whether two strings have the same character frequencies.


def is_anagram(first_string, second_string):
    # If the strings do not have the same length, they cannot be anagrams.
    if len(first_string) != len(second_string):
        return False

    # Count how many times each character appears in the first string.
    frequency = {}
    for char in first_string:
        frequency[char] = frequency.get(char, 0) + 1

    # Reduce the counts as we read the second string.
    for char in second_string:
        if char not in frequency:
            return False

        frequency[char] -= 1
        if frequency[char] < 0:
            return False

    # Every character count must be zero for the strings to be anagrams.
    return all(count == 0 for count in frequency.values())


# Example one: "listen" and "silent" are anagrams.
first_word = "listen"
second_word = "silent"
print("Are the strings anagrams?", is_anagram(first_word, second_word))
