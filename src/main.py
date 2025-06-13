from src.game import TicTacToe

def main():
    game = TicTacToe()

    # Choose number of players
    while True:
        try:
            numPlayers = int(input("Enter number of players (1 or 2): "))
            if not 1 <= numPlayers <= 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter numbers 1 or 2.")
            continue  
        break

    # Play game
    while True:
        if numPlayers == 1 and game.current_player == "O":
            game.make_computer_move()
        else:
            game.display()
            print(f"Player {game.current_player}'s turn.")
            try:
                row = int(input("Enter row number (0-2): "))
                if not 0 <= row <= 2:
                    raise ValueError
                col = int(input("Enter col number (0-2): "))
                if not 0 <= col <= 2:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter numbers 0-2.")
                continue
            if not game.make_player_move(row, col):
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