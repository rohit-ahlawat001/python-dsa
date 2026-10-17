# array problems from the the CampusX DSA for AI series

### 1. Find the Largest Number in a List

numbers = [12, 45, 7, 89, 34, 95, 62, 57]

# write code here
largest = numbers[0]
for element in numbers[1:]:
    if element > largest:
        largest = element
print(f'Largest element: {largest}')


### 2. Count Occurrences of an Element
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2

# write code here
count = 0
for element in numbers:
    if element == target:
        count += 1
print(f'Occurrences of {target}: {count}')