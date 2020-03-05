def checkio(number: int) -> int:
    result = list(str(number))
    print(result) # ['1', '2', '3', '4', '0', '5']

    result2 = [int(item) for item in result]  # Перевод списка строк в список чисел
    #print(result2) # [1, 2, 3, 4, 0, 5]
    z = 1
    for i in result2:
        if i > 0:
            z *=i
    print(z) # 120
    return z


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1



"""
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.

Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

Входные данные: Положительное целое число.
Выходные данные: Произведение цифр как целочисленное (int).

Примеры:

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1

Зачем это нужно: Эта задача может научить вас как использовать простую конвертацию типов данных.

Предусловия: 0 < number < 106
"""