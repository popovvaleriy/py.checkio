from functools import reduce
from itertools import combinations
import re
def checkio(number):
    l = []
    
    number_sort = number
    count = 2
    while number_sort >= 2:  
        if number_sort % count == 0:
            number_sort = number_sort//count
            if count != 1 and count != number:
                if count <= 10:
                    l.append(count)
        else:
            count = count + 1
    print(l, "list")
    
    Empty = []
    for s, e in combinations(range(len(l) + 1), 2):
        substr = l[s:e]
        if reduce(lambda x, y: x*y, substr) == number: # умножение элементов
            Empty = substr #если один из вариантов перебора соответствует number то оставляем его
    print(Empty, "Empty")

    if len(Empty) == 0:
        print("None")
        return 0    
    
    s = []
    for i in Empty:
        s.append(str(i))
        result = (','.join(s)).replace(",", '')    
    
    result_filt1 = re.sub('222', '8', str(result))       #'33', '9'
    result_filt2 = re.sub('33', '9', str(result_filt1)) #'23', '6'
    result_filt3 = re.sub('23', '6', str(result_filt2))#'222', '8'
    result_filt4 = re.sub('22', '4', str(result_filt3)) #'22', '4'
    print(list(result_filt4))

    end_list = []
    for i in list(result_filt4):
        end_list.append(int(i))
    end_list.sort()    
    print(end_list, "end_list")

    s2 = []
    for i in end_list:
        s2.append(str(i))
        result = (','.join(s2)).replace(",", '')    
    print(result, "result")
    print("---------------------")    
    return int(result)
    
if __name__ == '__main__':
    assert checkio(1536) #==3888
    assert checkio(288) #==489
    assert checkio(12) #==26
    assert checkio(1024) #==2888
    #assert checkio(560) #== 2578
    #assert checkio(3645) #==5999
    #assert checkio(20) #== 45, "1st example"
    #assert checkio(1680) #== 5678
    #assert checkio(21) #== 37, "2nd example"
    #assert checkio(17) #== 0, "3rd example"
    #assert checkio(33) #== 0, "4th example"
    #assert checkio(3125) #== 55555, "5th example"
    #assert checkio(9973) #== 0, "6th example"


"""
Дано число N. Необходимо найти наименьшее положительное целое число X, такое, что произведение его цифр будет равна N.
Если X не существует - верните 0.

Рассмотрим пример. N = 20. Мы можем разложить данное число, как 2*10, но 10 - это не цифра.
Также можно разложить N, как 4*5 или 2*2*5. Наименьшее число для 2*2*5 - это 225, для 4*5 -45. Результат 45.

Примечания: Не забудьте о простых числах и будьте аккуратны с вечными петлями.

Входные данные: Число N, как целое число (int).
Выходные данные: Число X, как целое число (int).

Примеры:
checkio(20) == 45
checkio(21) == 37
checkio(17) == 0
checkio(33) == 0

Зачем это нужно: В этой задаче вы попрактикуетесь работь с числами.
А также можете сравнить, как решать задачи в лоб или подумать более хитрое решение.

Предусловия:
9 < N < 105.
"""

"""
# разложение числа на множители
    i = 2
    mnogitel = []
    while i * i <= number:
        while number % i == 0:
            mnogitel.append(i)
            number = number // i
        i = i + 1
    if number > 1:
        mnogitel.append(number)
    print(mnogitel)


>>> from functools import reduce  # умножить все элементы в списке вместе
>>> reduce(lambda x, y: x*y, [1,2,3,4,5,6])
720
"""
