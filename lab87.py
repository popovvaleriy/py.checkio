from typing import Iterable

def except_zero(items: list) -> Iterable:
    l = []
    for i in items:
        if i > 0:
            l.append(i)
    l_sort = sorted(l)
    print(l_sort)

    for i in range(len(items)):
        if items[i] == 0:
            l_sort.insert(i, 0)
            
    #l_sort.insert(2, '*')
    print(l_sort)
    
    return l_sort


if __name__ == '__main__':
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]


"""
Сортировать числа в массиве. Но положение нулей не должно быть изменено.

Вход: список.
Выход: Iterable (кортеж, список, итератор ...).

Example:

except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
except_zero([0, 2, 3, 1, 0, 4, 5]) == [0, 1, 2, 3, 0, 4, 5]
"""
