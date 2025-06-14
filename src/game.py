import random
from src.utils import print_board, check_winner, is_full

class TicTacToe:
    def __init__(self):
        self.board = [["   " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    # Play the game
    def play(self):
        num_players = self.get_valid_number("Enter number of players (1 or 2): ", 1, 2)

        while True:
            if num_players == 1 and self.current_player == "O":
                self.handle_computer_turn()
            else:
                self.handle_player_turn()

            if self.check_game_over():
                break
            self.switch_player()
            
    # Make player move
    def make_player_move(self, row, col):
        if self.board[row][col] == "   ":
            self.board[row][col] = " " + self.current_player + " "
            return True
        return False
    
    # Make computer move
    def make_computer_move(self):
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == "   "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = " " + self.current_player + " "
            return True
        return False

    # Switch player
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # Get winner
    def get_winner(self):
        return check_winner(self.board)

    # Check for draw
    def is_draw(self):
        return is_full(self.board) and not self.get_winner()

    # Display the board
    def display(self):
        print_board(self.board)

    # Get valid number input
    def get_valid_number(self, prompt, min_value, max_value):
        while True:
            try:
                value = int(input(prompt))
                if not (min_value <= value <= max_value):
                    raise ValueError
                return value
            except ValueError:
                print(f"Invalid input. Enter a number between {min_value} and {max_value}.")

    # Get valid move from player
    def get_valid_move(self):
        while True:
            row = self.get_valid_number("Enter a row number (0-2): ", 0, 2)
            col = self.get_valid_number("Enter a col number (0-2): ", 0, 2)
            if self.make_player_move(row, col):
                return
            else:
                print("Invalid input. Enter a move for an empty cell.")

    # Handle player turn
    def handle_player_turn(self):
        self.display()
        print(f"Player {self.current_player}'s turn.")
        self.get_valid_move()

    # Handle computer turn
    def handle_computer_turn(self):
        print("Computer's turn.")
        self.make_computer_move()

    # Check if the game is over
    def check_game_over(self):
        winner = self.get_winner()
        if winner:
            self.display()
            print(f"Player {winner} wins!")
            return True
        if self.is_draw():
            self.display()
            print("It's a draw!")
            return True
        return False