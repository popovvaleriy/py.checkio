def max_digit(number: int) -> int:
    return int(max(str(number)))


if __name__ == '__main__':
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1


"""
У вас есть номер, и вам нужно определить, какая цифра в этом номере самая большая.

Вход: положительный Int.
Output: An Int (0-9).

Example:
max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1

"""
