# Creating a list
courses = ['History', 'Math', 'Science', 'Art']

courses_2 = ['Phy Ed', 'History']

nums = [1, 5, 2, 4, 3]
# Using an Index to print values
# print(courses[0])

# Using an Index to print a range of values doesn't include the 2nd index. Prints 0 and 1. This is process is called slicing
# print(courses[0:2])

# Adds Physics to the list
# courses.append('Physics')

# Adds a new value to the list in a specific position
# courses.insert(0, 'Physics')

# Able to insert a list within a list
# courses.insert(0, courses_2)

# Adds the values from the second list courses_2 to the original courses list
# courses.extend(courses_2)

# If you need to remove something from the list
# courses.remove('Math')

#Pops the last value off the list
# popped = courses.pop()
# print(popped)

#Reverses the list
# courses.reverse()

# Sorts the list of strings into alphabetical order and ints into ascending order 
# courses.sort()
# nums.sort()

# Sorts the list in reverse alphabetically
# sorted_courses = sorted(courses)
# print(sorted_courses)

#Min, Max and Sum of num list
# print(min(nums))
# print(max(nums))
# print(sum(nums))

for item in courses:
    print(item)

print(courses)