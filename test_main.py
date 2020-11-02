from unittest import TestCase
from main import Roll, Game

class TestGame(TestCase):
    def test_roll_strike(self):
        player1 = Game()
        player1.roll(10)
        equal_frame = Frame(10,0,0)
        assertEqual(player1.frames[0], equal_frame)

    def test_roll_strike_2more_rolls(self):
        player1 = Game()
        player1.roll(10)
        equal_frame = Frame([10,0], 0)
        assertEqual(player1.frames[0], equal_frame)
