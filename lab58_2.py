def is_palindromic(text):
    return text == text[::-1]

def longest_palindromic(text):
    l = []
    pol = []
    for i in range(len(text)+1):
        for j in range(len(text)+1):
            l.append(text[i:j])
    #print(l)
    for i in l:
        #print(i)
        if is_palindromic(i) and len(i) >= 2:
            pol.append(i)
    print(pol) # ['aba', 'aca', 'ada']
    if len(pol)>0:
        count = 0
        for i in pol:
            print(len(i))
            count = count + len(i)
        print(count)

        #print(count/len(pol[0]))
        if count/len(pol[0]) == len(pol[0]):
            #print(pol[0])
            return pol[0]
        else:
            #print(max(pol,key=len)) # максимальный по длине вложенный список
            return max(pol,key=len)
    else:
        print(text[0])
        return text[0]


if __name__ == '__main__':
    assert longest_palindromic("abc")
    #assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    #assert longest_palindromic("fbacaba") # == "bacab"
    #assert longest_palindromic("abacada") #== "aba", "The First"
    #assert longest_palindromic("aaaa") == "aaaa", "The A"


"'a', 'c', 'a', 'b', 'c', 'b', '_', '", "', 'a', 'b', 'a', '_'"
"""
https://py.checkio.org/ru/mission/the-longest-palindromic/

Напишите функцию, которая найдет самый длинный палиндром в строке.
Постарайтесь быть максимально эффективными при решении этой задачи.
Если найдено более одной палиндром с максимальной длинной, то верните тот, который находится ближе к началу строки.

Входные параметры: Строка.
Выходные параметры: Строка.

Примеры:

longestPalindromic("artrartrt") == "rtrartr"
longestPalindromic("abacada") == "aba"
longestPalindromic("aaaa") == "aaaa"

Предусловия: 1 < |text| ≤ 20
Текст содержит только ASCII символы.
"""
