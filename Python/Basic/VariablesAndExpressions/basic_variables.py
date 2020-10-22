f=0
# print(f)

#Prints f as a string which says hello world
#Shows that even if a variable has been declared you can redeclare
# f="Hello World"
# print(f)

#Note you cannot concantenate str and int objects in python you will need to convert both outputs

#Function
#showing that the f string within the function is seperate to the f string out of the function
def someFunction():
    #Effects all f variables within the function and out of the function
    global f
    f="Hows it going?"
    print(f)

#Calling someFunction() 
someFunction()
print(f)