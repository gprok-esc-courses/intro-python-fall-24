from tkinter import Tk, Label, Button, Text, END

def click_me():
    txt = text.get("1.0", END)
    print(txt)
    message.configure(text=txt.strip())

window = Tk()
window.geometry("400x400")

message = Label(window, text="Hello World!")
message.grid(row=0, column=0)

text = Text(window, height=2, width=10)
text.grid(row=1, column=0)

button = Button(window, text="Click me", command=click_me)
button.grid(row=2, column=0)

window.mainloop()