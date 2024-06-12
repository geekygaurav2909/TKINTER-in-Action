from tkinter import *

window = Tk()
window.title("My first Python GUI Program")
window.minsize(width=600, height= 600)

# Label

my_label = Label(text= "I am Simply a Label", font=("Arial", 24, "bold"))
my_label.pack()

def name_change():
    value = input.get()[len("Enter the name: "):]
    print(value)
    my_label.config(text=value)


button = Button(text= "Click me", command= name_change)
button.pack()


# Entry

input = Entry(width=30)
input.insert(END, "Enter the name: ")
input.pack()

# Text

my_text = Text(height=5, width=30)
my_text.focus()
my_text.insert(END, "Example of multi-line text")
print(my_text.get("1.0", END))
my_text.pack()

# Spin 

def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_= 0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale

def scale_used(value):
    print(value)


value = Scale(from_=0, to= 10, command=scale_used)
value.pack()

# Check button

def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(text="Is on", variable=checked_state, command=checkbutton_used)
checked_state.get()
check_button.pack()


# Radio button

def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text= "Option 1", value =1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text= "Option 2", value= 2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List box

def list_used(event):
    print(listbox.get(listbox.curselection()))


listbox  = Listbox(height=4)
fruits = ["Apple", "Papaya", "Orange", "Banana"]
for items in fruits:
    listbox.insert(fruits.index(items), items)

listbox.bind("<<ListboxSelect>>", list_used)
listbox.pack()

window.mainloop()
