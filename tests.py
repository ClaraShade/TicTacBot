import unittest
from Enemy import GameScore

class TestMethods(unittest.TestCase):

    def test_winning_eval_rows(self):
        win_gamescore = GameScore(3)
        win_gamescore.squares = [['_', 'o', 'o'], ['_', '_', '_'], ['_', '_', '_']]

    def test_blocking_eval_rows(self):
        block_gamescore = GameScore(3)
        block_gamescore.squares = [['_', '_', 'x'], ['_', 'x', '_'], ['_', '_', '_']]

print(TestMethods.test_winning_eval_rows())



