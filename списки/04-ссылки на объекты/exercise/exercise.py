import pytest


def make_list(count):
    pass


def test_make():
    l = make_list(10)

    assert l == [[] for _ in range(10)]
    l[2].append(True)
    l[1].append('False')

    assert l == [ [True, 'False'] for _ in range(10)]
