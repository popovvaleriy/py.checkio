def count_consecutive_summers(num):
    count_all = num
    len_num = range(num)
    print(len_num)
    print(len_num[1:])
    summ = 0
    count_in = 0
    m = 1

    while count_all > 0:
        for i in len_num[m:]:
            print(summ)
            if summ <= num:
                summ = summ + i
            if summ == num:
                count_in = count_in + 1
        summ = 0
        print(summ)
        m = m + 1
        count_all = count_all - 1

    count_in = count_in + 1    
    print(count_in)
    return count_in


if __name__ == '__main__':
    assert count_consecutive_summers(15)
    #assert count_consecutive_summers(42) #== 4
    #assert count_consecutive_summers(99) #== 6
    #assert count_consecutive_summers(1) #== 1

"""
Положительные целые числа могут быть выражены в виде сумм последовательных положительных целых чисел различными способами.
Например, 42 можно выразить как такую сумму четырьмя различными способами:
(а) 3 + 4 + 5 + 6 + 7 + 8 + 9,
(б) 9 + 10 + 11 + 12,
(в) 13 + 14 +15 и
(d) 42.
Как показывает последнее решение (d), любое положительное целое число всегда можно тривиально выразить в виде одноэлементной суммы,
состоящей только из этого целого числа.

Вычислите, сколько разных способов это можно выразить как сумму последовательных натуральных чисел.

Input: Int.
Output: Int.

Example:
count_consecutive_summers(42) == 4
count_consecutive_summers(99) == 6

Precondition: Input is always a positive integer.

The mission was taken from Python CCPS 109 Fall 2018. It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""
