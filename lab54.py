def reverse_roman(roman_string):
    Numeral_Value = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    Numeral_List = ['I','V','X','L','C','D','M']
    print(list(roman_string))
    roman_string_list = list(roman_string)

    l = []
    
    for z in roman_string_list:
        for i,g in Numeral_Value.items():
            if z == i:
                l.append(g)
    print(l)
    summa = []
    for i in range(len(l) - 1):
        if l[i] < l[i+1] and l[i] != 0:
            print(l[i+1] - l[i])
            summa.append(l[i+1] - l[i])
            l[i] = 0
            l[i + 1] = 0
            i = i + 2
        else:
            print(l[i])    
            summa.append(l[i])
            l[i] = ''
    summa.append(l[-1])
    print(l)
    print(sum(summa))
    return sum(summa)

if __name__ == '__main__':
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'

"""
В CheckiO миссие Roman Numerals Вам нужно было преобразовать десятичное число в соответствующее ему римское.
Здесь Вам необходимо сделать все то же с точностью до наоборот.

Вам предоставляется римское число в виде строки. Ваша задача заключается в том,
чтобы преобразовать это число в ее десятичное представление.

Натуральное римское число в контексте этой миссии будет содержать римские цифры в соответствии с приведенной ниже таблице
и следовать правилам непозиционной системы счисления.

Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Входные данные: Римское число в виде строки.
Выходные данные: Десятичное представление римского числа как int.

Пример:
reverse_roman('VI') == 6
reverse_roman('LXXVI') == 76
reverse_roman('CDXCIX') == 499
reverse_roman('MMMDCCCLXXXVIII') == 3888

Предварительное условие:
len(roman_string) > 0
all(char in "MDCLXVI" for char in roman_string) == True
0 < reverse_roman(roman_string) < 4000
"""
