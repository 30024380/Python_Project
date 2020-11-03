# This program will take the basic input of the user and an if statement will initiate with the proper response

# Initiates the program by greeting the user and asking for the users name
print('Greetings user. Please input your name')
response=input('Name: ') # This will apply the users name to the variable 'response'

# Prints out the message 'Welcome' and uses the variable response divided by a space for clean presentation
print('Welcome '+response)

# At this point the IF statement will start to operate as it will be giving you a message followed by a question.
print('You will be given a choice between 2 options, these will be split apart using the numbers 1 and 2\n')
print('If this code is being executed and the option shows that means that an IF statement is currently being executed,\n')

print('Do you like dogs?')

# Another variable that will take the users input and save it to the variable
initialize=input('1 means yes, 2 means no ')

# the IF statement
if initialize=="1":
    print("Awesome, dogs are cute aren't they?") # This message is printed to the console if the user selects the first option.
elif initialize=="2":
    print("That's fine, you might be a cat person then.") # This message is printed to the console if the users selects the second option.
else:
    print('That was not a valid option, please try again.') # This is basically an error thats printed to the console if the user doesn't select the correct option.


