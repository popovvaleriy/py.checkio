def first_word(text: str) -> str:
    result = text.split(" ")

    print(result[0])
    return result[0]


if __name__ == '__main__':
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"

"""
Дана строка и нужно найти ее первое слово.
Это упрощенная версия миссии First Word.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.

Входные параметры: Строка.
Выходные параметры: Строка.
Пример:

first_word("Hello world") == "Hello"

How it is used: The first word is a command in command line.
Precondition: Text can contain a-z, A-Z and spaces.
"""
