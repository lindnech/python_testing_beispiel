from programm import *

def test_plusmal():
    assert plusmal(2,3) == (2+3)*2

def test_unterschreiben(x):
    assert "10" ==  "Heute_10"

def test_kubieren1(x):
    assert 2**3 == 8

def test_kubieren2(x):
    assert 3**3 == 27

def test_testfehler():
    assert add(2,3) == 7