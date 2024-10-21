from tkinter import Misc, Tk, Label, Button, Frame, Variable
from typing import Any, Literal
from models import Game

def play_again():
    print("Play Again")
    for b in btn_list:
        b['state'] = "normal"
        b.config(text="-")
    game.start_new_round()
    play_label.config(text="X plays")

def btn_clicked(row, col):
    print("BTN:", row, col)
    current = game.current_player.symbol
    result = game.play(row, col)
    print(result)
    if result:
        row -= 1
        col -= 1
        btn_list[row * 3 + col].config(text=current)
        winner = game.check_winner()
        if winner is not None:
            play_label.config(text=winner.name + " wins!")
            for b in btn_list:
                b['state'] = "disabled"
        else:
            play_label.config(text=game.current_player.symbol + " plays")
            err_label.config(text="Game in progress")
    else:
        err_label.config(text="Invalid position")

    


game = Game()
game.start_new_game('john', 'mary')
game.start_new_round()
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

