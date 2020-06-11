from typing import Iterable

def is_ascending(items: Iterable[int]) -> bool:
    for i in range(len(items)-1):
        print(items[i])
        if items[i + 1] > items[i]:
            continue
        else:
            return False    
    return True


if __name__ == '__main__':
    assert is_ascending([-5, 10, 99, 123456]) == True
    #assert is_ascending([99]) == True
    #assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    #assert is_ascending([]) == True
    #assert is_ascending([1, 1, 1, 1]) == False

"""
Определите, является ли последовательность элементов элементов восходящей,
так что каждый ее элемент строго больше (и не просто равен) элемента, предшествующего ему.

Ввод: итерируемый с целыми числами.
Выход: Bool.

Example:
is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
is_ascending([]) == True
is_ascending([1, 1, 1, 1]) == False


The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""
