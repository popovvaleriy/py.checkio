import re
def first_word(text: str):
    text2 = text.strip('.' + ' ')
#    print(text2)
    l = []
    for i in text2:
        if i == " " or i == ".":
            break
        else:
#            print(i)
            l.append(i)        
#    print(l)
    result = ','.join(l)
    result2 = re.sub(r',', '', result) 
    print(result2)
    return result2


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    assert first_word("Hello world")
    assert first_word(" a word ")
    assert first_word("don't touch it")
    assert first_word("greetings, friends")
    assert first_word("... and so on ...")
    assert first_word("hi")
    assert first_word("Hello.World")
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""
Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:
    В строке могут встречатся точки и запятые
    Строка может начинаться с буквы или, к примеру, с пробела или точки
    В слове может быть апостроф и он является частью слова
    Весь текст может быть представлен только одним словом и все

Входные параметры: Строка.
Выходные параметры: Строка.

Пример:
first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"

How it is used: first word is a command in command line
Precondition: text can contain a-z A-Z , . ' 
"""
