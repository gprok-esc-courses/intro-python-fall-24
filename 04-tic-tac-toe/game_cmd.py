from models import Player, Game

print("TIC TAC TOE Game")
name1 = input("First player: ")
name2 = input("Second player: ")

game = Game()
game.start_new_game(name1, name2)
game.start_new_round()


while True:
    game.print_board()
    print(game.current_player, "plays")
    row = int(input("Row: "))
    col = int(input("Col: "))
    result = game.play(row, col) 
    if not result:
        print("Invalid position")
    else:
        winner = game.check_winner()
        if winner is not None:
            game.print_board()
            print(winner, "wins!")
            # update score and display the score
            break
        else:
            # check for Tie
            pass


