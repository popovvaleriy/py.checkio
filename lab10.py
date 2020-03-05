import re

def correct_sentence(text):
    result = text.replace('.', '')
    f = result[0].capitalize()
    print(f + result[1:] + ".")
    return f + result[1:] + "."

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    assert correct_sentence("greetings, friends")
    assert correct_sentence("Greetings, friends")
    assert correct_sentence("Greetings, friends.")
    assert correct_sentence("hi")
    assert correct_sentence("welcome to New York")  
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""
На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так,
чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку,
то добавлять еще одну не нужно, это будет ошибкой

Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).

Пример:
correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и . 
"""
