#
# Name: Blake Jensen
# Student ID: 30006830
#

# Arrays

# This program demonstrates how arrays work in Python

# An array works very similar to a list or dictionary
cars = ["Ferrari", "Pagani", "Koenigsegg", 
"Lamborghini", "Mercedes Benz", "BMW", "Audi", 
"Apollo", "Nissan", "Toyota", "Subaru",
"Honda", "Mazda", "Hyundai", "Scion", "Ford"]

# however the way an array works differently to lists and dictionaries is that you are able to store many values inside it and call to them using an index
x = cars[2]
y = cars[6]
z = cars[12]
# Note: when calling an item from the array, remember that everything begins at 0 in code, therefore the first item has the number value ID of 0, then to 1 and so on

print(x, y, z)

# we can also ask for the len of the array so that we have a clear indication of how many values are stored
length = len(cars)

# if this is correct it should print the number 16 indicating that there is 16 values stored in the array
print(length) 

# we can also print each item in the array using a for loop like so
for a in cars:
    print(a)