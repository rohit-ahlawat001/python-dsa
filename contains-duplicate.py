# Python List and hashmap problems

# Problem Two: Contains Duplicate - Check whether any value appears more than once.


def contains_duplicate(numbers):
    # A set stores only unique values.
    # It is useful here because we can quickly check whether a value is already present.
    seen_numbers = set()

    # Look at every number in the input list one by one.
    for number in numbers:
        # If this number is already in the set, it appears more than once.
        if number in seen_numbers:
            return True

        # This is the first time we have seen this number,
        # so add it to the set for future checks.
        seen_numbers.add(number)

    # If the loop finishes, every value appeared only once.
    return False


# Example one: 1 appears twice, so the result is True.
numbers_with_duplicate = [1, 2, 3, 1]
print("Has duplicate:", contains_duplicate(numbers_with_duplicate))

# Example two: all values are different, so the result is False.
numbers_without_duplicate = [1, 2, 3, 4]
print("Has duplicate:", contains_duplicate(numbers_without_duplicate))