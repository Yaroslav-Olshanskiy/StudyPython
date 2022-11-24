import pytest

list_ = ['a', 'bbbbbb', 'cccc']
list_.sort(key=len)
print(list_)