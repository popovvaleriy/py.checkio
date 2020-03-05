import re
def checkio(n, m):
    min_max = [n,m]
    find_min = min(min_max) # 117
    find_max = max(min_max) # 17    
    one_chi = bin(find_max)[2:] # 0b1110101  со срезом:1110101
    two_chi = bin(find_min)[2:] # 0b10001    со срезом:10001
    razn = abs(len(one_chi) - len(two_chi)) # 2

    null = '0'
    if razn > 0:
        two_chi_null = null*razn + str(two_chi) # 0010001
    else:
        two_chi_null = two_chi
    print(two_chi_null)


    one_chi_range = range(len(one_chi)) # range(0, 9)
    two_chi_range = range(len(two_chi_null)) # range(0, 9)
    
    l = []
    for i in two_chi_range:
        if two_chi_null[i] == one_chi[i]:
            l.append(0)
        else:
            l.append(1)
    print(l.count(1)) # [1, 1, 0, 0, 1, 0, 0], 3 единицы
    return l.count(1)

if __name__ == '__main__':
    assert checkio(117, 17) #== 3, "First example"
    assert checkio(1, 2) #== 2, "Second example"
    assert checkio(16, 15) #== 5, "Third example"

    
"""
https://py.checkio.org/ru/mission/hamming-distance2/

Расстояние Хэмминга между двумя двоичными числами - это число позиций, в которых биты различаются (прочитать о расстоянии Хэмминга на Википедии).
Для примера:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

Даны два положительных целых числа (N, M) в десятичном виде.
Вам необходимо подсчитать расстояние Хэмминга между этими двумя числами в двоичном виде.

Входные данные: Два аргумента, как целые числа (int).
Выходные данные: Расстояние Хэмминга, как целое число (int).

Примеры:
checkio(117, 17) == 3
checkio(1, 2) == 2
checkio(16, 15) == 5

Зачем это нужно: Это базис для кодов Хэмминга и других программ корректировки ошибок. 
Также расстояние Хэмминга используют, как измерения разницы в генетике (в более общей форме).

Предусловия:
0 < n < 106
0 < m < 106

0b1110101
0b10001

"""
