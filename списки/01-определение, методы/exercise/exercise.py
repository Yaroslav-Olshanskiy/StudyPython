import pytest
import math


def get_square_roots(digit):
    if digit > 0:
        sqrt = math.sqrt(digit)
        return [-sqrt, sqrt]
    if digit == 0:
        return [0]
    if digit < 0:
        return []



def test_1():
    assert get_square_roots(-1) == []
    assert get_square_roots(0) == [0]
    assert get_square_roots(25) == [-5.0, 5.0]
