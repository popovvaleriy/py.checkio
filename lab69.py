import re

def double_substring(line):
    l = []
    print(line)

    for i in range(len(line)):
        for j in range(len(line)+1):
            if j > i:
                l.append(line[i:j])
    print(l)

    z = []
    for i in l:
        if l.count(i) > 1:
            z.append(i)
    print(z, 'z')

    spisok = []
    for i in z:
        result3 = re.findall(i, line)
        if len(result3) > 1:
            spisok.append(i)
    print(spisok)

    #result = [word for word in l if l.count(word)>1] # выводим значения, количество которых больше чем 1
    if len(spisok) > 0:
        #print(max(result, key = len))
        print(max(spisok, key = len))
        #return max(result, key = len)
        return len(max(spisok, key = len))
    else:
        print('0')
        return 0

if __name__ == '__main__':
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"

"""
Double Substring
Существует четыре миссии связанные с анализом частей строк.
Все они были созданы за один день и не требуют более одного дня для своего решения.
Эти миссии можно с легкостью преодолеть посредством простого перебора символов.
Но, возможно, есть вариант получше?
(У Вас может еще не быть доступа ко всем этим миссиям, но по мере открытия островов на карте он будет предоставлен)

Третья миссия является единственной в серии, где Вам необходимо вернуть не саму подстроку, а ее длину.
Вы должны найти подстроку, которая повторяется больше одного раза в данной строке и при этом повторения друг на друга не накладываются.
Например, в строке "abcab" самая длинная подстрока, которая повторяется более одного раза, это "ab",
поэтому ответом должно быть число 2 (длина "ab").

Входные данные: Строка.
Выходные данные: Целое число.

Пример:
double_substring('aaaa') == 2
double_substring('abc') == 0
double_substring('aghtfghkofgh') == 3 # fgh
"""
