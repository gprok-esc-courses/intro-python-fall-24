from tkinter import Misc, Tk, Label, Button, Frame, Variable
from typing import Any, Literal

# class GameButton(Button):
#     def __init__(self, master: None, brow: 0, bcol: 0) -> None:
#         super().__init__(master, text='-')
#         self.brow = brow
#         self.bcol = bcol

#     def on_click(self, event):
#         print(self.brow, self.bcol)

def play_again():
    print("Play Again")

def btn_clicked(row, col):
    print("BTN:", row, col)


window = Tk()
window.title('Tic Tac Toe')

play_label = Label(window, text="X plays")
play_label.grid(row=1, column=1)

frame = Frame(window)
btn_list = [] 
for r in range(1, 4):
    for c in range(1, 4):
        b = Button(frame, text='-', command=lambda row=r, col=c: btn_clicked(row, col))
        b.grid(row=r, column=c)
        btn_list.append(b)
frame.grid(row=2, column=1)

err_label = Label(window, text="Game in progress")
err_label.grid(row=3, column=1)

play_again_btn = Button(window, text="Play Again", command=play_again)
play_again_btn.grid(row=4, column=1)

window.mainloop()

