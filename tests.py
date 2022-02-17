import unittest
from Enemy import GameScore


class TestMethods(unittest.TestCase):

    def test_winning_eval_rows(self):
        win_gamescore = GameScore(3)
        win_gamescore.squares = [['_', 'o', 'o'], ['_', '_', '_'], ['_', '_', '_']]
        self.assertEqual([[10005, 0, 0], [5, 5, 5], [5, 5, 5]], win_gamescore.eval_rows('o'))

    def test_blocking_eval_rows(self):
        block_gamescore = GameScore(3)
        block_gamescore.squares = [['_', 'x', 'x'], ['_', '_', '_'], ['_', '_', '_']]



