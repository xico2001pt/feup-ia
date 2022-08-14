from copy import deepcopy

# a)    
#       Representation: ([[int]], player)
#       Initial State: ([[0]], 1)
#       Final States: a vertical, horizontal or diagonal line with 4 consecutive pieces of the same player
#
#       Operators           Pre-conditions      Effects
#       Play X              board[0][X] = 0     board[Y][X] = player; player = (player % 2) + 1

class ConnectFour:
    def __init__(self, rows, columns, starter_player):
        self.rows = rows
        self.columns = columns
        self.starter_player = starter_player
    
    def game_cycle(self):
        total_pieces = self.rows * self.columns
        played_pieces = 0
        self.new_game(self.starter_player)

        while played_pieces < total_pieces:
            move = ConnectFour.choose_move(self.board, self.player)
            if not ConnectFour.is_valid_play(self.board, move):
                continue

            self.play(move)
            played_pieces += 1
            if self.is_game_over(self.player):
                print(f'Player {self.player} won!')
                return

            self.player = (self.player % 2) + 1

        print("The game resulted in a draw :/")
    
    def new_game(self, starter_player):
        self.player = starter_player
        self.reset_board()
    
    def play(self, column):
        row = ConnectFour.get_valid_row(self.board, column)
        self.board[row][column] = self.player
        
    def reset_board(self):
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def is_game_over(self, player):
        # TODO
        return False
    
    def copy(game):
        result = ConnectFour(game.rows, game.columns, game.starter_player)
        result.player = game.player
        result.board = deepcopy(game.board)
        return result

    def is_valid_play(board, column):
        return board[0][column] == 0

    def get_valid_row(board, column):
        rows = len(board)
        for i in range(rows):
            row = rows - i - 1
            if board[row][column] == 0:
                return row
        return -1

    def choose_move(board, player):
        return 0

if __name__ == "__main__":
    game = ConnectFour(6, 7, 1)
    game.game_cycle()
