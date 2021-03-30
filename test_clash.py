import unittest
from clash import Clash
from warrior_factory import WarriorFactory
from unittest.mock import patch
import random


class TestClashUnittest(unittest.TestCase):

    def setUp(self):
        print('Unittest start')
        player1 = WarriorFactory.create_by_id(1)
        player2 = WarriorFactory.create_by_id(2)
        self.test = Clash(player1, player2)

    def tearDown(self):
        del self.test
        print('Unittest done\n')

    def test_init(self):
        self.assertEqual(self.test.escapes, 0)
        self.assertEqual(self.test.result, 0)

    @patch("builtins.input", return_value='F')
    def test_runaway_false(self, mock_input):
        print(" Trying 'F'")
        self.assertIs(self.test.runaway(), False)

    @patch("builtins.input", return_value='R')
    def test_runaway_true(self, mock_input):
        print(" Trying 'R'")
        self.assertIs(self.test.runaway(), True)

    @patch("builtins.input", side_effect=['', 'f'])
    def test_runaway_else(self, mock_input):
        print(" Trying any key")
        self.assertIsNot(self.test.runaway(), True)

    @patch("builtins.input", return_value=1)
    def test_runaway_int(self, mock_input):
        print(" Trying integer")
        with self.assertRaises(AttributeError):
            self.test.runaway()

    @patch("builtins.input", return_value='r')  # RUN      runaway == True,  low_hp == True
    def test_low_hp_Run(self, mock_input):
        self.test.player1.hp = 15
        self.assertIs(self.test.low_hp(), True)

    @patch("builtins.input", return_value='f')  # FIGHT
    def test_low_hp_Fight(self, mock_input):
        self.test.player1.hp = 15
        self.assertIs(self.test.low_hp(), False)

    def test_low_hp_pass(self):
        self.test.player1.hp = 55
        self.assertFalse(self.test.low_hp())
        self.test.escapes = 2
        self.test.player1.hp = 14
        self.assertFalse(self.test.low_hp())


if __name__ == '__main__':
    unittest.main()

"""
Pytest
"""


class TestClashPytest:

    def setup(self):
        print('Pytest start')
        player1 = WarriorFactory.create_by_id(1)
        player2 = WarriorFactory.create_by_id(2)
        self.test = Clash(player1, player2)

    def teardown(self):
        self.test.your_choice = input      # Так ли?
        print('Test done\n')

    def test_low_hp_1(self):
        self.test.player1.hp = random.randint(50, 100)
        assert self.test.escapes == 0

    def test_low_hp_2(self, monkeypatch):               # для автоматического заполнения input
        monkeypatch.setattr('builtins.input', lambda: "f")
        self.test.player1.hp = random.randint(15, 49)
        self.test.low_hp()
        self.test.player1.hp = 15                       # тест второй смывки при пограничном здоровье
        self.test.low_hp()
        self.test.player1.hp = random.randint(1, 14)
        self.test.low_hp()
        point1 = self.test.escapes
        self.test.player1.hp = random.randint(1, 14)    # тест третьей смывки
        self.test.low_hp()
        self.test.player1.hp = 0                        # тест смывки мертвеца
        self.test.low_hp()
        point2 = self.test.escapes
        assert point1 == 2 and point2 == 2

    def test_combat_run(self):
        self.test.low_hp = True
        assert self.test.result == 0

    def test_combat_fail(self):
        self.test.player1.hp = 10
        self.test.p1_damage = 0
        self.test.player1.chance = 0
        self.test.p2_damage = 10
        self.test.combat()
        assert self.test.result == 1

    def test_combat_win(self):
        self.test.p1_damage = 10
        self.test.player2.hp = 10
        self.test.p2_damage = 0
        self.test.player2.chance = 0
        self.test.combat()
        assert self.test.result == 2
