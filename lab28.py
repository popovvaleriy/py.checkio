def easy_unpack(elements: tuple) -> tuple:
    l = []
    d = []


    for i in elements:
        l.append(i)
    print(l)
    print(range(len(l)))

    for i in range(len(l)):
        if i == 0:
            d.append(l[i])
        if i == 2:
            d.append(l[i])
    d.append(l[-2])
    print(d)

    print(tuple(d))
    return tuple(d)



if __name__ == '__main__':
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) #== (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) #== (1, 1, 1)
    assert easy_unpack((6, 3, 7)) #== (6, 7, 3)
    print('Done! Go Check!')

"""
Ваше задание здесь создать функцию, которая получает массив(tuple)
и возвращает набор с 3 элементами - первым, третьим, вторым с конца.

Входные данные: Набор длинной не менее 3 элементов.
Выходные данные: Набор элементов.

Пример:

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)
"""
