
class Player:
    def __init__(self, name, symbol) -> None:
        self.name = name
        self.score = 0
        self.symbol = symbol

    def __str__(self) -> str:
        return self.name + ' [' + self.symbol + ']'
    
class Game:
    def __init__(self) -> None:
        self.player_x = None
        self.player_o = None
        self.current_player = None
        self.board = None

    def start_new_game(self, name1, name2):
        self.player_x = Player(name1, 'X')
        self.player_o = Player(name2, 'O')

    def start_new_round(self):
        self.board = [['-']*3 for i in range(3)]
        self.current_player = self.player_x

    def play(self, row, col) -> bool:
        row = row - 1
        col = col - 1
        if row < 0 or row  > 2 or col < 0 or row > 2:
            return False
        if self.board[row][col] != '-':
            return False
        self.board[row][col] = self.current_player.symbol
        self.current_player = self.player_x \
                if self.current_player == self.player_o \
                else self.player_o
        return True 
    
    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=' ')
            print()

    def find_user_by_symbol(self, symbol):
        if symbol == 'X':
            return self.player_x
        elif symbol == 'O':
            return self.player_o
        else: 
            return None 

    def check_winner(self) -> Player:
        """
        Check each row, column, and diagonal, to see if they have same values,
        and also that these values are not the dash '-' which measn empty.
        """
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and \
                self.board[row][0] == self.board[row][2] and \
                self.board[row][0] != '-':
                return self.find_user_by_symbol(self.board[row][0])
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] and \
                self.board[0][col] == self.board[2][col] and \
                self.board[0][col] != '-':
                return self.find_user_by_symbol(self.board[0][col])
        # Check diagonals
        if self.board[0][0] == self.board[1][1] and \
                self.board[0][0] == self.board[2][2] and \
                self.board[0][0] != '-':
                return self.find_user_by_symbol(self.board[0][0])
        if self.board[0][2] == self.board[1][1] and \
                self.board[0][2] == self.board[2][0] and \
                self.board[0][2] != '-':
                return self.find_user_by_symbol(self.board[0][2])
        return None
        

if __name__ == '__main__':
    a = Player('John', 'X')
    print(a)