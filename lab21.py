import re
def checkio(words: str) -> bool:
    result = words.split(' ')  #['one', 'two', '3', 'four', 'five', 'six', '7', 'eight', '9', 'ten', 'eleven', '12']

    l = []  # временный список для отсеивания цифр
    l2 = []  # временный список для группировки слов между цифрами
    l3 = []  # временный список для вывода количество слов идущих подряд
    
    for i in range(len(result)):
        if result[i].isalpha():
            l.append(result[i])
        else:
            l.append(';')
    #print(l)  #['one', 'two', ';', 'four', 'five', 'six', ';', 'eight', ';', 'ten', 'eleven', ';']
    result = ((','.join(l)).replace(",",' ')).split(';')
    #one,two,;,four,five,six,;,eight,;,ten,eleven,; -->  one two ; four five six ; eight ; ten eleven ;  -->  ['one two', 'four five six', 'eight', 'ten eleven', '']
    for i in result:
        word = i.rstrip().strip()
        #print(word)
        l2.append(word)
    print(l2)  #['one two', 'four five six', 'eight', 'ten eleven', '']

    for i in range(len(l2)):
        count = len(re.findall(r'\w+',l2[i]))#количество слов в списке ['one two', 'four five six', 'eight', 'ten eleven', '']
        if count >= 3:
            l3.append(count)
    print(l3)
    if l3 == []:
        return False
    else:
        for i in l3:
            if i >= 3:
                return True
            else:
                return False     



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""
Давайте научим наших роботов отличать слова от чисел.
Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.

Примеры:
checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False


Зачем это нужно: Эта задача подскажет вам как работать со строками и покажет некоторые полезные функции.

Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
0 < len(words) < 100
"""
