line = list('sdsffffse')

def long_repeat(line):   
    c = []

    if len(line) == 1:  #Если список не более 1го символа
        longest = 1
        print('1')
        return 1
    if len(line) == 0:  #Если список не более 1го символа
        longest = 0
        print('0')
        return 0
    
    for i in range(len(line) - 1):  # 9 символов, нач. с нуля 0,1,2,3,4,5,6,7,8
        if i == 0:  #Приравнивается к 0му индексу и добавляется 1 с список "c" иначе при повторе в начале выдаст ошибку
            c.append(1)         
        if line[i] != line[i + 1]: #Добавляется 1 если след. символ не совпадает с предыдущим             
            c.append(1)                         
        else:  #иначе, при совпадении элементов               
            print(line[i])                
            c[-1] = c[-1] + 1  #В списке "с" увеличивающийся элемент находится в конце и постоянно увеличивается счетчик
                
    print(c)
    print(max(c))
    return(max(c))

long_repeat(line)


"""
необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв.
Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa".
Последняя подстрока является самой длинной, что и делает ее ответом.

Входные данные: Строка.
Выходные данные: Целое число.

assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
"""
