from main.calc import Calc

def test_add_01():
    assert Calc(9,2).add() == 11

def test_add_02():
    assert Calc(-9,2).add() == -7

def test_dif_01():
    assert Calc(9,2).dif() == 7

def test_dif_02():
    assert Calc(-9,2).dif() == -11
