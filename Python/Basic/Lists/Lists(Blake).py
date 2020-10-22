#
# Name: Blake Jensen
# Student ID: 30006830
#

# Lists

# This program is demonstrating how lists are created using Python.

# First we determine the name of the list we are going to create
list1 = ["Apple", "Banana", "Carrot", "Durian", "Eggplant", "Feijoa"]
numbers = [1,2,3,4,5,6,7,8,9,10]

# Then we call the lists using the print() function
print(list1)
print(numbers)

# The above code will retrieve the entire list, but if you want to retrieve a singular part of the list you can do so like this
print(list1[2]) # since everything in code starts at 0 this will retrieve 'Carrot' and not 'Banana'
print(numbers[-2]) # this will select a number from the opposite side of the start, so starting from 10 and going down

# Lists differ from dictionaries as dictionaries are able to take both a string and an integer value
