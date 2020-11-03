# Name: Blake Jensen
# Student ID: 30006830
#

# Methods

# First a class will need to be defined
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is a definition, therefore I am defining that the function I am creating can be used somewhere else in the code.
    # As you can see it has a special message using what I name for the variables
    # Everything that is inside the def function is known as the method.
    def myfunction(self):
        print("Hi, this is " + self.name + ". Please be nice to him. He is " + str(self.age) + " years old")

    def myfunction1(self):
        print("Now, this is " + self.name + ". He's a really cool person. He is " + str(self.age) + " years old")

# Both p1 and p2 are variables that are assigned values 
p1 = Person("John", 21)
p2 = Person("Dave", 24)

# Then we take the variables with values and assign them to the functions that we created in the class. 
p1.myfunction()
p2.myfunction1()