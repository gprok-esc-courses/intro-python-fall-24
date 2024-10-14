from tkinter import Tk, Label, Button

def btn_clicked():
    print("Clicked")

window = Tk()
window.geometry('400x250')
label = Label(window, text="Hello World!")
label.grid(row=1, column=1)
btn = Button(window, text="Click Me", command=btn_clicked)
btn.grid(row=2, column=1)

window.mainloop()



