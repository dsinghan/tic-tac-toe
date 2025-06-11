from src.utils import print_board, check_winner, is_full

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_winner(self):
        return check_winner(self.board)

    def is_draw(self):
        return is_full(self.board) and not self.get_winner()

    def display(self):
        print_board(self.board)