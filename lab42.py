from itertools import product
def repeat_inside(line):
    result = ''
    print(range(len(line))) # range(0, 10)
    print(len(line)) # 10
    
    for i in range(len(line)):
        print(i)
        for j in range(len(line) - i):
            print(j)
            print(range(len(line)-i))
            s = line[i:i + j + 1]
            print(s)
            for k in range(2, len(line) // len(s) + 1):
                ls = s * k
                if ls in line and len(ls) > len(result):
                    result = ls
    print(result) #abcabc
    return result


"""
    result = ''
    R = range(len(string)) # range(0, 10)

    for i, j, k in product(R, R, R):    
       pattern = string[i:j]*(k+2)  # i началаьная часть, j конечная, k размер слова
       print(pattern)

       if string.count(pattern):
           print(string.count(pattern))
           result = max(result, pattern, key=len)
           print(result)

    return result
"""

if __name__ == '__main__':
    #assert repeat_inside('aaaaa') #== 'aaaaa', "First"
    #assert repeat_inside('aabbff') #== 'aa', "Second"
    #assert repeat_inside('aababcc') #== 'abab', "Third"
    #assert repeat_inside('abc') #== '', "Forth"
    assert repeat_inside('abcabcabab') #== 'abcabc', "Fifth"
"""
Существует четыре миссии связанные с анализом частей строк.
Все они были созданы за один день и не требуют более одного дня для своего решения.
Эти миссии можно с легкостью преодолеть посредством простого перебора символов.
Но, возможно, есть вариант получше? (У Вас может еще не быть доступа ко всем этим миссиям,
но по мере открытия островов на карте он будет предоставлен)
Это четвертая и последняя миссия серии. Если в первой миссии Вам нужно было найти повторяющиеся буквы,
то здесь Вам необходимо разыскать повторяющуюся последовательность в подстроке.
У меня есть небольшой пример: в строке "abababc" - "ab" является последовательностью,
которая повторяется более одного раза, поэтому ответом будет "ababab".

Входные данные: Строка.
Выходные данные: Строка.

Пример:
repeat_inside('aaaaa') == 'aaaaa'
repeat_inside('aabbff') == 'aa'
repeat_inside('aababcc') == 'abab'
repeat_inside('abc') == ''
repeat_inside('abcabcabab') == 'abcabc'

"""


"""
    longest = ''
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            substrn = substr = line[i:j]
            for _n in range(2, len(line) // (j - i) + 1):
                substrn += substr
                if substrn in line:
                    if len(substrn) > len(longest):
                        longest = substrn
                else:
                    break

    return longest
"""


"""
    result = ''
    print(range(len(line))) # range(0, 10)
    print(len(line)) # 10
    
    for i in range(len(line)):
        print(i)
        for j in range(len(line) - i):
            print(j)
            print(range(len(line)-i))
            s = line[i:i + j + 1]
            print(s)
            for k in range(2, len(line) // len(s) + 1):
                ls = s * k
                if ls in line and len(ls) > len(result):
                    result = ls
    print(result) #abcabc
    return result
"""
