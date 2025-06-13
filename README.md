# Tic Tac Toe

Python tic tac toe game.

## Features

- Two-player mode (X and O)
- Single-player mode (X)
- Input validation
- Board display after each move
- Win and draw detection
- Computer moves
- Unit tests included

## Project Structure

```
tic-tac-toe/
├── src/
│   ├── main.py        # Gameplay
│   ├── game.py        # Game logic
│   └── utils.py       # Utility functions
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
3. **Follow the prompts** to choose the game mode and enter your moves.

## Running Unit Tests

From the project root, run:
```sh
python3 -m unittest discover
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
