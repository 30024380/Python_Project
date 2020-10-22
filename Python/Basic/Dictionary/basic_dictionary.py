student = {'name': 'John', 'age': 22, 'courses': ['Math', 'English']}

# for key, value in student.items():
#     print(key, value)

# Updates the data within the dictionary
student.update({'name': 'Jesse', 'age': 23, 'courses': ['Art', 'Crump Dance Battle']})

# Deletes the data within the dictionary if specified
del student['age']

# Prints the amount of keys within the dictionary
# print(len(student))

# Prints only the values in the dictionary
# print(student.values())

# Prints keys and items
# print(student.items())

print(student)