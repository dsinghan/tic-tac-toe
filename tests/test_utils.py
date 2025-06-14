import unittest
from src.utils import check_winner, is_full

class TestUtils(unittest.TestCase):
    def test_check_winner_row(self):
        board = [
            [" X ", " X ", " X "],
            ["   ", " O ", "   "],
            ["   ", "   ", " O "]
        ]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_column(self):
        board = [
            [" O ", " X ", "   "],
            [" O ", " X ", "   "],
            [" O ", "   ", " X "]
        ]
        self.assertEqual(check_winner(board), "O")

    def test_check_winner_diagonal(self):
        board = [
            [" X ", " O ", "   "],
            ["   ", " X ", " O "],
            ["   ", "   ", " X "]
        ]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_none(self):
        board = [
            [" X ", " O ", " X "],
            [" O ", " X ", " O "],
            [" O ", " X ", " O "]
        ]
        self.assertIsNone(check_winner(board))

    def test_is_full_true(self):
        board = [
            [" X ", " O ", " X "],
            [" O ", " X ", " O "],
            [" O ", " X ", " O "]
        ]
        self.assertTrue(is_full(board))

    def test_is_full_false(self):
        board = [
            [" X ", " O ", " X "],
            [" O ", "   ", " O "],
            [" O ", " X ", " O "]
        ]
        self.assertFalse(is_full(board))

if __name__ == "__main__":
    unittest.main()