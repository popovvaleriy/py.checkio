def beginning_zeros(number: str) -> int:
    count = 0
    for item in number:
        if item == '0':
            count +=1
        else:
            print(count, 'count')
            return count
    print(count, 'count')
    return count


if __name__ == '__main__':
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4


"""
У вас есть строка, состоящая только из цифр.
Вам нужно найти, сколько нулевых цифр ("0") находится в начале данной строки.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4

Ввод: строка, состоящая из цифр.
"""
