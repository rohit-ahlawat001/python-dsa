# Python List and hashmap problems

# Problem One: Two Sum - Find two numbers whose sum equals a target.


def two_sum(numbers, target):
	# This dictionary will remember each number and its index.
	# Example: after reading [2], it will contain {2: 0}.
	number_to_index = {}

	# enumerate gives us both the index and the number at that index.
	for index, number in enumerate(numbers):
		# If number + another_number == target,
		# then another_number must be target - number.
		needed_number = target - number

		# Check whether the number we need was seen earlier.
		if needed_number in number_to_index:
			# Return the two positions, not the two numbers.
			return [number_to_index[needed_number], index]

		# Save the current number so a later number can use it.
		number_to_index[number] = index

	# Return an empty list when no pair adds up to the target.
	return []


# Sample input: 2 + 4 = 6.
list_one = [2, 4]
target_number = 6

# The answer is [0, 1] because 2 is at index 0 and 4 is at index 1.
answer = two_sum(list_one, target_number)
print("Indexes of the two numbers:", answer)
