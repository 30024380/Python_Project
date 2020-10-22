#
# Name: Blake Jensen
# Student ID: 30006830
#

# Classes

# This program demonstrates how classes operate

# much like in C# the way to define a class is by starting it with 'class' and then naming the class itself afterwards, for this I am naming it 'MyClass'
class MyClass():
    # Inside here we can then define a function and start adding functionality to the method of the class
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # Now that the class has some variables inside it, lets add something that would be executed when we call the class

    def callThis(self):
        print("Vehicle: " + self.make + "\nModel: " + self.model)
        # Tip: \n means new line, therefore when the function is called and prints to the console it will add a new line with the following text

# Now we call the class and give it values to both variables we added at the beginning
car1 = MyClass("Ferrari", "488 Pista")

# now we call the values we just added combined with the function
car1.callThis()

# Now when the script is called it should read in the console that the vehicle is a ferrari 488 pista