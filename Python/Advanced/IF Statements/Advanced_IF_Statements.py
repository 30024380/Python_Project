# Field for tkinter imports 
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

# Dimensions & Styling of window
root = Tk()
root.title("Advanced IF Statements")
root.configure(bg="pink")

myFont = font.Font(family='Lato')

e = Text(root, bg="grey", width=66, wrap=WORD, font=myFont)
e.grid(row=0, column=0, columnspan=3)
e.insert(END, "Click a button to be presented with a messagebox querying you about a certain question.")
# Def functions
def firstIF():
    response = messagebox.askyesnocancel("Ask Question", "Yes, No, or Cancel?")
    if response == True:
        b = messagebox.askokcancel("ATTENTION!", "You clicked Yes")
    elif response == False:
        c = messagebox.askokcancel("ATTENTION!", "You clicked No")
    else:
        d = messagebox.askokcancel("ATTENTION!", "You clicked Cancel")

def secondIF():
    response2 = messagebox.askyesno("Next Question", "Is 5 greater than 0?")
    if response2 == True:
        a = messagebox.askokcancel("Correct!", "You are correct.")
    if response2 == False:
        a1 = messagebox.askokcancel("Incorrect!", "Everything begins at 0, therefore 5 is higher. Meaning you are wrong.")

def thirdIF():
    list1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    response3 = messagebox.askyesno("Question.", "Do you wish to view the list?")
    if response3 == True:
        e.delete('1.0', END)    
        e.insert(END, list1)
    elif response3 == False:
        a2 = messagebox.askokcancel("ATTENTION!", "Understood, click OK to continue back to the original frame.")
        e.delete('1.0', END)
        e.insert(END, "Click a button to be presented with a messagebox querying you about a certain question.")
        

# Buttons
button_activatequery = Button(root, text="First IF statement", padx=40, pady=20, font=myFont, command=firstIF)
button_activatequery2 = Button(root, text="Second IF statement", padx=40, pady=20, font=myFont, command=secondIF)
button_activatequery3 = Button(root, text="Third IF statement", padx=40, pady=20, font=myFont, command=thirdIF)

button_activatequery.grid(row=1, column=0)
button_activatequery2.grid(row=1, column=1)
button_activatequery3.grid(row=1, column=2)

root.mainloop()