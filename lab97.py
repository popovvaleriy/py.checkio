def is_all_upper(text: str) -> bool:
    if text == '':
        print(False)
        return False
    elif text.isdigit():
        print(False)
        return False
    elif text.isupper():
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == '__main__':
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False

"""
Проверьте, содержит ли данная строка все символы в верхнем регистре.
Если строка пуста или в ней нет буквы - функция должна вернуть False.

Вход: строка.
Выход: логическое значение.

Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == False

Precondition: a-z, A-Z, 1-9 and spaces 
"""
