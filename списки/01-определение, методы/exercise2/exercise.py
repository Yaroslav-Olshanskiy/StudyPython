import pytest


def get_equals_length(list_):
    list_.sort(key=len)
    digit = len(list_[-1])
    for i in list_:
        if len(i) < digit:
            return i + '__' #тут ошибка
        else:
            return i


def test_1():
    assert get_equals_length(['a', 'b', 'ccc']) == ['a__', 'b__', 'ccc']
    l = ['a', 'b', 'ccc']
    l_copy = l[:]
    get_equals_length(l)
    assert l_copy == l
    assert get_equals_length([1, 'uqw', 2, 'c']) == []
    assert get_equals_length([]) == []
    assert get_equals_length(['A', 'dddd', 'c%']) == ['A___', 'dddd', 'c%__']
