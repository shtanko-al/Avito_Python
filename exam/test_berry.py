import pytest
from ver_2 import berry_coun


def test_1():
    my_input = [0, 1]
    expect = 'raise ImportError'
    assert berry_coun(my_input) == expect


def test_2():
    my_input = [1, 1, 1, 1, 1]
    expect = 0
    assert berry_coun(my_input) == expect


def test_3():
    my_input = [1, 1, 5, 1, 1]
    expect = 1
    assert berry_coun(my_input) == expect


def test_4():
    my_input = [1, 1, 5, 2, 1]
    expect = 2
    assert berry_coun(my_input) == expect


def test_5():
    my_input = [2, 1, 1, 6, 7]
    expect = 4
    assert berry_coun(my_input) == expect


if __name__ == '__main__':
    pytest.main()
