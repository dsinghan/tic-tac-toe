# Tic Tac Toe

Tic Tac Toe game written in Python.

## Features

- Two-player mode
- Single-player mode
- Input validation
- Board display
- Win and draw detection
- Computer moves
- Unit tests

## Project Structure

```
tic-tac-toe/
├── src/
│   ├── main.py
│   ├── game.py        # Game logic
│   └── utils.py       # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_game.py 
│   └── test_utils.py
└── README.md
```

### Running the Game

From the project root, run:
```sh
python3 -m src
```

### Running Tests

From the project root, run:
```sh
python3 -m unittest discover tests
```