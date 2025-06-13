import unittest
from src.game import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_initial_state(self):
        game = TicTacToe()
        self.assertEqual(game.current_player, "X")
        self.assertTrue(all(cell == "   " for row in game.board for cell in row))

    def test_make_move_and_switch(self):
        game = TicTacToe()
        self.assertTrue(game.make_player_move(0, 0))
        self.assertEqual(game.board[0][0], " X ")
        game.switch_player()
        self.assertEqual(game.current_player, "O")

    def test_winner_row(self):
        game = TicTacToe()
        for col in range(3):
            game.make_player_move(0, col)
        self.assertEqual(game.get_winner(), "X")

    def test_winner_column(self):
        game = TicTacToe()
        for row in range(3):
            game.make_player_move(row, 0)
        self.assertEqual(game.get_winner(), "X")

    def test_winner_diagonal(self):
        game = TicTacToe()
        moves = [(0, 0), (1, 1), (2, 2)]
        for i, (r, c) in enumerate(moves):
            game.make_player_move(r, c)
        self.assertEqual(game.get_winner(), "X")

    def test_invalid_move(self):
        game = TicTacToe()
        self.assertTrue(game.make_player_move(0, 0))
        self.assertFalse(game.make_player_move(0, 0))

    def test_draw(self):
        game = TicTacToe()
        moves = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        for i, (r, c) in enumerate(moves):
            game.make_player_move(r, c)
            if i < len(moves) - 1:
                game.switch_player()
        self.assertTrue(game.is_draw())

if __name__ == "__main__":
    unittest.main()