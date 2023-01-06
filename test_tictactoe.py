import pytest

import TicTacToe_2016 as ttt

class TestZone:
    def test_create_grid(self):
        b = ttt.create_grid()
        print(b)
        assert b == [[" ", " ", " "],
                     [" ", " ", " "],
             [" ", " ", " "]]

    def test_iswinner(self):
        b = ttt.create_grid()
        b[0][0] = "X"
        b[0][1] = "X"
        b[0][2] = "X"

        winner = ttt.iswinner(b, "X", "O")
        assert not winner

    def test_isnotwinner(self):
        b = ttt.create_grid()

        winner = ttt.iswinner(b, "X", "O")
        assert winner

    def test_printpretty(self, capsys):
        b = ttt.create_grid()
        ttt.printpretty(b)
        captured = capsys.readouterr()
        assert captured.out == "Here is the playboard: \n---+---+---\n   |   |  \n---+---+---\n   |   |  \n---+---+---\n   |   |  \n---+---+---\n"