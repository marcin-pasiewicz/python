import unittest
import random_game


class TestGame(unittest.TestCase):
    def test_input(self):
        result = random_game.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = random_game.run_guess(0, )
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = random_game.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = random_game.run_guess('11', 5)
        self.assertFalse(result)


if __name__ == '__random_game__':
    unittest.random_game()
