Numeral_Value = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'L':50,'C':100,'D':500,'M':1000}

def checkio(data):
    data_list = list(str(data)) #[8, 80, 800, 3000]   

    list_int = []
    count = 1
    for i in data_list[::-1]:
        list_int.append(int(i)*count)
        count = count*10
    print(list_int)        
    l = []
    
    count2 = 10
    count3 = 50

    for elem in list_int:
        if 0 < elem < 10:
            for k,v in Numeral_Value.items():
                if elem == v:
                    #print(k)
                    l.append(k)
    for elem in list_int[1:]:
        if elem >= 10:
            if elem == 10 or elem == 50 or elem == 100 or elem == 500 or elem == 1000:
                res = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(elem)]
                l.append(res)
            if elem == 0:
                print('')
            if elem == count3 - count2: # для 4
                result_des = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count2)]
                result_five = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count3)]
                #print(result_des + result_five)
                l.append(result_des + result_five)
            if elem < count3 - count2 and elem != 10 and elem != 100 and elem != 1000: # для 1-3
                result_des = (list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count2)])
                count = elem // count2
                #print(result_des*count)
                l.append(result_des*count)
            if elem == (count3 * 2) - count2: # для 9
                result_des = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count2)]
                result_five = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count3*2)]
                #print(result_des2 + result_five2)
                l.append(result_des + result_five)
            if count3 < elem < ((count3 * 2) - count2): # для 6-8
                result_five = list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count3)]
                result_des = (list(Numeral_Value.keys())[list(Numeral_Value.values()).index(count2)])
                count = (elem - count3) // count2
                #print(result_five3 + result_des3*count)
                l.append(result_five + result_des*count)
        count2 = count2 * 10
        count3 = count3 * 10
    print(l)
    rome = []
    for i in l[::-1]:
        rome.append(i)
    result_rome = ','.join(rome)
    print(result_rome.replace(",", ''))    
    return result_rome.replace(",", '') #MMMDCCCLXXXVIII

if __name__ == '__main__':
    #assert checkio(6) #== 'VI', '6'
    #assert checkio(10)
    #assert checkio(602)
    #assert checkio(76) #== 'LXXVI', '76'
    #assert checkio(164) #== 'CLXIV'
    #assert checkio(3810) #== 'MMMDCCCX'
    assert checkio(100)
    #assert checkio(500)
    #assert checkio(499) #== 'CDXCIX', '499'
    #assert checkio(38)
    #assert checkio(3888) #== 'MMMDCCCLXXXVIII', '3888'

"""
Римские цифры пришли к нам из древней римской системы счета.
Они основаны на особых буквах алфавита, которые в различных сочетаниях,
путем суммирования (а иногда и разницы) описывают различные числа.
Первые 10 римских чисел это:
I, II, III, IV, V, VI, VII, VIII, IX, and X.

Римская система счета имеет десятичное основание, но она непозиционная и не включает в себя 0 (ноль).
Римские числа образуются путем комбинации следующих семи символов:
Символ	Значение
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.

Вх. данные: Число, как целочисленное (int).
Вых. данные: Римское число, как строка (str).
Предусловия: 0 < number < 4000
"""

"""
            #for k,v in Numeral_Value.items():
            #    if elem == v:
            #        #print(k)
            #        l.append(k)
"""
