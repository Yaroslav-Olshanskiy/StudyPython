import pytest
import math


def get_square_roots(digit):
    return []


def test_1():
    assert get_square_roots(-1) == []
    assert get_square_roots(0) == [0]
    assert get_square_roots(25) == [-5.0, 5.0]
