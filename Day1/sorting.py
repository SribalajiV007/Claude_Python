# numbers = [47, 10, 3, 25, 8]


# numbers.sort()
# print(numbers)  # [3, 8, 10, 25, 47] → ascending

# numbers.sort(reverse = True)
# print(numbers)  # [47, 25, 10, 8, 3] → descending

# numbers1 = [47, 10, 3, 25, 8]
# new_list = sorted(numbers)
# print(numbers)
# print(new_list)

marks = [78, 45, 92, 61, 88, 34, 75]

marks.sort()
print(marks)

marks.sort(reverse = True)
print(marks)

print(marks[0])
print(marks[6])

print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")