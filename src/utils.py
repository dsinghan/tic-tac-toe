def print_board(board):
    print("    0   1   2")
    print(" ", "-" * 13)
    for row in range(len(board)):
        print(row, "|" + "|".join(board[row]) + "|")
        print(" ", "-" * 13)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "   ":
            winner = board[i][0][1]
            board[i][0] = board[i][1] = board[i][2] = "-" + winner + "-"
            return winner
        if board[0][i] == board[1][i] == board[2][i] != "   ":
            winner = board[0][i][1]
            board[0][i] = board[1][i] = board[2][i] = "-" + winner + "-"
            return winner
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "   ":
        winner = board[0][0][1]
        board[0][0] = board[1][1] = board[2][2] = "-" + winner + "-"
        return winner
    if board[0][2] == board[1][1] == board[2][0] != "   ":
        winner = board[0][2][1]
        board[0][2] = board[1][1] = board[2][0] = "-" + winner + "-"
        return winner
    # No winner found
    return None

def is_full(board):
    return all(cell != "   " for row in board for cell in row)