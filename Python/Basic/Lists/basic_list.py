# Creating a list
courses = ['History', 'Math', 'Science', 'Art']

courses_2 = ['Phy Ed', 'History']

# Adds the values from the second list courses_2 to the original courses list
courses.extend(courses_2)

for item in courses:
    print(item)

print(courses)