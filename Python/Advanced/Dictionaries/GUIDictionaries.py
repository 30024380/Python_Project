from tkinter import *

# Create a variable to use for styling the application
yes = Tk()
yes.geometry("600x500") # This manages the window size
yes.title("GUI Testing") # This gives the window it's title

# These are the dictionaries, they differentiate from lists as they are able to contain a integer value after the string value
item1 = {"John Woodstock": 332516, "Steve Block": 554125, "Ken Redwood": 120054, "David Havelock": 557481}
item2 = {"Apple", "Banana", "Orange", "Cherry"} # Not all dictionaries must require an integer value after the string value.
item3 = {"stuff": 1234, "more stuff": 1234, "extra stuff": 1234, "yes": 1234}

a = Listbox(yes, bg="grey", fg="white", width=100)
a.grid(row=0, column=0, columnspan=3)

a.insert(END, "Please select a Dictionary to display")
a.insert(END, "Please be aware that Dicitonaries will have a string value before an integer")

def button_dictionary1insert():
    a.delete(0, END)
    a.insert(END, item1)

def button_dictionary2insert():
    a.delete(0, END)
    a.insert(END, item2)

def button_dictionary3insert():
    a.delete(0, END)
    a.insert(END, item3)

# This creates the buttons for the GUI to be used.
# However they haven't been implemented into the app itself.
button_dictionary1 = Button(yes, text="First Dictionary", padx=31, pady=30, command=button_dictionary1insert)
button_dictionary2 = Button(yes, text="Second Dictionary", padx=22, pady=30, command=button_dictionary2insert)
button_dictionary3 = Button(yes, text="Third Dictionary", padx=28, pady=30, command=button_dictionary3insert)

# This places the buttons on the grid that was created with the variable at the start
button_dictionary1.grid(row=1, column=0)
button_dictionary2.grid(row=2, column=0)
button_dictionary3.grid(row=3, column=0)

yes.mainloop()