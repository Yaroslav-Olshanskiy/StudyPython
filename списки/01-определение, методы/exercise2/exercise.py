import pytest


def get_equals_length(list_):
    if len(list_):
        biggest = len(max(list_, key=len))
        result = []
        for i in list_:
            if len(i) < biggest:
                result.append(i + "_" * (biggest - len(i)))  # +++++
            else:
                result.append(i)
        return result
    else:
        return []



def test_1():
    assert get_equals_length(['a', 'b', 'ccc']) == ['a__', 'b__', 'ccc']
    l = ['a', 'b', 'ccc']
    l_copy = l[:]
    get_equals_length(l)
    assert l_copy == l
    assert get_equals_length([1, 'uqw', 2, 'c']) == []
    assert get_equals_length([]) == []
    assert get_equals_length(['A', 'dddd', 'c%']) == ['A___', 'dddd', 'c%__']
