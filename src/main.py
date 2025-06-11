from src.game import TicTacToe

def main():
    game = TicTacToe()
    while True:
        game.display()
        print(f"Player {game.current_player}'s turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers 0-2.")
            continue
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue
        if not game.make_move(row, col):
            print("Cell already taken. Try again.")
            continue
        winner = game.get_winner()
        if winner:
            game.display()
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            game.display()
            print("It's a draw!")
            break
        game.switch_player()

if __name__ == "__main__":
    main()