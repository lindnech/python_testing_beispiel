from programm import *

def test_plusmal():
    assert plusmal(2,3) == (2+3)*2

def test_unterschreiben():
    assert unterschreiben("Heute") ==  "Heute_unterschrieben"

def test_kubieren1():
    assert kubieren(2) == 2**3

def test_kubieren2():
    assert kubieren(3) == 3**3

# def test_testfehler():
#     assert plusmal(2,3) == 7
