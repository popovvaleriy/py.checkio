def middle(text):
    print(text)
    if len(text) == 1:
        print(text)
        print("_____")
        return text
    if len(text) % 2 == 0:
        print(text[int(len(text)/2 -1):int(len(text)/2+1)])
        print("_____")
        return text[int(len(text)/2 -1):int(len(text)/2+1)]
    else:
        print(text[int(len(text)/2)])
        return text[int(len(text)/2)]
        print("_____")


if __name__ == '__main__':
    assert middle('example') == 'm'
    assert middle('test') == 'es'    
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'


"""
У вас есть определенная строка, в которой вы хотите найти средние символы.
Строка может состоять как из одного слова или даже нескольких символов, так и быть целым предложением.
Если длина строки четная - вам необходимо вернуть два средних символа, если же нечетная - только один.
Более наглядно это описано в Примерах.

Входные данные: Строка.
Выходные данные: Средние символы.

Примеры:
middle('example') == 'm'
middle('test') == 'es'    
middle('very-very long sentence') == 'o'
middle('I') == 'I'
middle('no') == 'no'

Как это используется: Для работы с текстами.

Предусловия:
1 <= длина строки <= 100 
"""
