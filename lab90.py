from typing import Tuple

def sum_by_types(items: list) -> Tuple[str, int]:
    
    return ('', 0)


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2', 3]) == ('12', 3)
    assert sum_by_types(['1', '2', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")



"""
У вас есть список. Каждое значение из этого списка может быть либо строкой, либо целым числом.
Ваша задача здесь - вернуть два значения. Первый - это объединение всех строк из данного списка.
Второй является суммой всех целых чисел из данного списка.

Входные данные: массив строк и целых чисел
Вывод: список или кортеж

Example:
sum_by_types([]) == ['', 0]
sum_by_types([1, 2, 3]) == ['', 6]
sum_by_types(['1', 2, 3]) == ['1', 5]
sum_by_types(['1', '2', 3]) == ['12', 3]
sum_by_types(['1', '2', '3']) == ['123', 0]
sum_by_types(['size', 12, 'in', 45, 0]) == ['sizein', 57]

How it’s used: (math is used everywhere)
Precondition: both given ints should be between -1000 and 1000 
"""
