
#functions are defined by the def key word
#Creating a function
def func1():
    print("This is a function")

#Function that takes an argument
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#function that returns a value
def cube(x):
    return x*x*x

#function that returns a value to the power of
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


#Calls the func1 function directly
# func1()
#Calls the function func1 within the print statement and returns the string within the function but it also returns none as the print executes because our function doesnt return a value
# print (func1())
#Function func1 is not being executed and is printing the value of func1
# print (func1)

# func2(10, 20)
# print(func2(10, 20))

#Prints the cube of 3
print (cube(3))
print (power(2))
print (power(2,3))
print (power(x=3, num=2))
