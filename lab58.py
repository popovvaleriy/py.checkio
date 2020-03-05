from itertools import combinations
def is_palindromic(text):
    return text == text[::-1]

def longest_palindromic(text):
    longest = ""
    for s, e in combinations(range(len(text) + 1), 2):  # combinations('ABCD', 2) --> AB AC AD BC BD CD
        substr = text[s:e]
        #print(substr)
        if is_palindromic(substr) and len(longest) < len(substr): # если substc палиондном и он больше текущего палиондрома в longest сетим в лонегст палиондром
            longest = substr
    #print(longest)
    return longest

"""
a
ab
aba
abac
abaca
abacad
abacada
b
ba
bac
baca
bacad
bacada
a
ac
aca
acad
acada
c
ca
cad
cada
a
ad
ada
d
da
a
aba
"""

if __name__ == '__main__':
    #assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    #assert longest_palindromic("fbacaba") # == "bacab"
    assert longest_palindromic("abacada") #== "aba", "The First"
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
