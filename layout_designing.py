from tkinter import *

window = Tk()
window.title("Layout Designing")
window.minsize(height=600,width=600)
window.config(padx=100,pady=200)

# Label
def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)


my_label = Label(text= "Layout Designing", font = ("Arial", 24, "bold"))
my_label.grid(row=0,column=0)

# button
button = Button(text= "Click me", command=button_clicked)
button.grid(row=1, column=1)

# button-2
new_button = Button(text= "New button", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry 

input = Entry(width=30)
input.grid(row=2, column=3)



window.mainloop()