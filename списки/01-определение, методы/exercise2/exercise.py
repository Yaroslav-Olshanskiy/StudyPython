import pytest


def get_equals_length(list_):
    # result = 0
    # if list_ == str(list_):
    #     for i in list_():
    #         if len(i) < result:
    #             result += 1
    #         return i + '_' + result
    len_ = 0
    for i in list_():
        len_ = len(i)


def test_1():
    assert get_equals_length(['a', 'b', 'ccc']) == ['a__', 'b__', 'ccc']
    l = ['a', 'b', 'ccc']
    l_copy = l[:]
    get_equals_length(l)
    assert l_copy == l
    assert get_equals_length([1, 'uqw', 2, 'c']) == []
    assert get_equals_length([]) == []
    assert get_equals_length(['A', 'dddd', 'c%']) == ['A___', 'dddd', 'c%__']
