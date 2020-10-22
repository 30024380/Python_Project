#
# Name: Blake Jensen
# Student ID: 30006830
#

# Declare variable and initialize
a=0
print(a)

# re-declaring the variable works
a="abc"
print(a)

# Error: variables of different types cannot be combined
# print("this is a string" + 123)
# This won't work, unless you're using something like Javascript where it would
# So then you need to add the correct converter like so:
print("this is a string " + str(123))

# Global vs. local variables in functions
def someFunction(): # Defines a function
    global a
    a="This is a definition"
    print(a)

someFunction()
print(a)

# deletes the variable and prints it
del a
# however this will print an error to the console since there is no variable to be printed to the console
print(a)
