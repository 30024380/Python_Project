from tkinter import *

yes = Tk()
yes.title("GUI Testing")

item1 = ["Car", "Truck", "Motorcycle", "Supercar"]
item2 = ["Apple", "Banana", "Orange", "Cherry"]
item3 = ["Fork", "Knife", "Spoon", "Ladle"]

a = Listbox(yes, bg="grey", fg="white", width=80)
a.grid(row=0, column=0, columnspan=3)

a.insert(END, "Please select a list")

def button_list1insert():
    a.delete(0, END)
    a.insert(END, item1)

def button_list2insert():
    a.delete(0, END)
    a.insert(END, item2)

def button_list3insert():
    a.delete(0, END)
    a.insert(END, item3)

def button_clear():
    a.delete(0, END)
    a.insert(END, "Please select a list")

button_list1 = Button(yes, text="First List", padx=31, pady=30, command=button_list1insert)
button_list2 = Button(yes, text="Second List", padx=22, pady=30, command=button_list2insert)
button_list3 = Button(yes, text="Third List", padx=28, pady=30, command=button_list3insert)
button_clear = Button(yes, text="Clear", padx=50, pady=30, command=button_clear)

button_list1.grid(row=1, column=0)
button_list2.grid(row=2, column=0)
button_list3.grid(row=3, column=0)
button_clear.grid(row=1, column=1)

yes.mainloop()