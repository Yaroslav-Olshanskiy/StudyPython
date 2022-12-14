import pytest


def make_list(value, count):
    pass


def test_make():
    assert make_list('b', 1) == [
        ['b', 'b', 'b'],
    ]
    assert make_list(False, 5) == [
        [False, False, False],
        [False, False, False],
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]
    assert make_list(1, '1') == []
    assert make_list(0, -1) == []
