# Tic Tac Toe

A simple console-based Tic Tac Toe game implemented in Python.

## Features

- Two-player mode (X and O)
- Input validation
- Board display after each move
- Win and draw detection
- Unit tests included

## Project Structure

```
tic-tac-toe/
├── src/
│   ├── main.py        # Entry point to play the game
│   ├── game.py        # Game logic (TicTacToe class)
│   └── utils.py       # Utility functions (board display, winner check)
├── tests/
│   ├── __init__.py
│   └── test_game.py   # Unit tests for the game logic
└── README.md
```

## How to Play

1. **Install Python 3** if you haven't already.
2. **Run the game** from the project root:
    ```sh
    python3 -m src.main
    ```
3. **Follow the prompts** to enter your moves (row and column numbers from 0 to 2).

## Running Unit Tests

From the project root, run:
```sh
python3 -m unittest discover
```
or
```sh
python3 -m unittest tests/test_game.py
```

## Example Gameplay

```
    0   1   2
  -------------
0 |   |   |   |
  -------------
1 |   |   |   |
  -------------
2 |   |   |   |
  -------------
Player X's turn.
Enter row (0-2):
