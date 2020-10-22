from tkinter import *

app = Tk()
app.geometry("485x500")
app.configure(bg="blue")

cars = ["Ferrari", "\nPagani", "\nKoenigsegg", 
"\nLamborghini", "\nMaserati", "\nBMW", "\nAudi", 
"\nApollo", "\nNissan", "\nToyota", "\nSubaru",
"\nHonda", "\nMazda", "\nHyundai", "\nScion", "\nFord"]

a = Listbox(app, fg="black", width=80)
a.grid(row=0, column=0, columnspan=3)

a.insert(END, "Please select an array from the buttons below")

def button_array1insert():
    a.insert(END, cars)

def button_return():
    a.delete(0, END)
    a.insert(END, "Please select an array from the buttons below")

def button_clear():
    a.delete(0, END)

button_array1 = Button(app, text="First Array", padx=31, pady=30, command=button_array1insert)
button_return = Button(app, text="Home", padx=31, pady=30, command=button_return)
button_clear = Button(app, text="Clear", padx=31, pady=30, command=button_clear)

button_array1.grid(row=3, column=0)
button_return.grid(row=3, column=1)
button_clear.grid(row=2, column=1, columnspan=2)


app.mainloop()