def checkio(array):
    l = []
    l2 = []

    if array == []:
        print('Empty')
        return 0
    else:
        for i in range(len(array)):
            l2.append(i)
        #print(l2)  #[0, 1, 2]
        for i in l2:
            if i%2 == 0:
                #print(array[i])
                l.append(array[i])
        print(l) #[1, 5]
        result = sum(l) * array[-1]
        print(result) #30
        return result
        
    
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) #== 30   "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) #== 30   "(1+5)*5=30"
    assert checkio([6]) #== 36   "(6)*6=36"
    assert checkio([]) #== 0   "An empty array = 0"


"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).

Примеры:

checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0

Зачем это нужно: Индексы и срезы - очень важные элементы программирования, как на Python, так и на других языках. Это поможет вам в дальнейшем.

Предусловия: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""
