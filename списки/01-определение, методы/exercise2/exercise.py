#import pytest


def get_equals_length(list_):
    list_.sort(key=len)
    biggest = len(list_[-1])
    for i in list_:
        if len(i) < biggest:
             list_.remove(str(i)) and list_.append(str(i) + '__')
    return list_
get_equals_length(['1111111111','22222'])



#def test_1():
    # assert get_equals_length(['a', 'b', 'ccc']) == ['a__', 'b__', 'ccc']
    # l = ['a', 'b', 'ccc']
    # l_copy = l[:]
    # get_equals_length(l)
    # assert l_copy == l
    # assert get_equals_length([1, 'uqw', 2, 'c']) == []
    # assert get_equals_length([]) == []
    # assert get_equals_length(['A', 'dddd', 'c%']) == ['A___', 'dddd', 'c%__']
