import re
from itertools import islice
from itertools import count

def house(plan):
    print(plan)

    if "#" not in plan:
        print("0")
        print("__________________")
        return 0

    g = []
    for i in plan:
        if i == '\n':
            g.append('|')
        else:
            g.append(i)
    #print(((",".join(g)).replace(",",""))[0:-1]) # |0000000|##00##0|######0|##00##0|#0000#0
    result = ((",".join(g)).replace(",",""))[0:-1]
    result_elem = result.split("|")
    print(result_elem, "result_elem")

    result_elem2 = []
    for i in result_elem:
        if i != "":
            result_elem2.append(i)
    print(result_elem2, "result_elem2") # ['0000', '0##0', '0000', '#00#', '0000'] убираем кавычки из списка

    k = []
    for i in result_elem2:
        for j in i:
            if j == "#":
               k.append(i.index(j))
               k.append(i.rindex(j))
    print(k)
    min_elem = min(k)
    print(min(k), "min(k)")
    max_elem = max(k)
    print(max(k), "max(k)")

    k2 = []
    for i in islice(count(), min(k), (max(k) + 1)):
        k2.append(i)
    print(k2, "k2")



    result_elem_int = []
    for i in result_elem2:
        k = re.sub(r'#', '1', i)
        result_elem_int.append(k)
    print(result_elem_int, "result_elem_int1") # ['0000', '0110', '0000', '1001', '0000'] заменяем # на "1" 

    for i in range(len(result_elem_int)): # убираем нулевые значения в начале списка
        if int(result_elem_int[i]) != 0:
            result_elem_int = result_elem_int[i:]
            break
    print(result_elem_int, "result_elem_int2")

    result_elem_int.reverse() # разворачиваем список и убираем нулевые значения в начале списка
    for i in range(len(result_elem_int)):
        if int(result_elem_int[i]) != 0:
            result_elem_int = result_elem_int[i:]
            break
    print(result_elem_int, "result_elem_int3")
        
    #result_elem_int.reverse() # возвращаем к исходному порядку
    #print(result_elem_int, "result_elem_int4")
    #print(max(result_elem_int), "max(result_elem_int)") # вывести максимальное значение по ключу
    #max_len = max(result_elem_int)

    #result2 = max_len.strip('0') #111111   убираем нулевые значения в начале и конце списка  
    #print(result2, "result2")
    result_finish = len(k2) * len(result_elem_int)
    print(result_finish)
    print("__________________")
    return result_finish
    

if __name__ == '__main__':

#    assert house('''
#00#0
#0#00
##000
#''') == 9

    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
000###0000
000#######
000###0000
''') == 21

    assert house('''
0##0
0000
#00#
''') == 12

    assert house('''
0000
0000
#000
''') == 1

    assert house('''
00#0
0#00
#000
''') == 9
    
"""
    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0
"""


"""
Остров был не близко, поэтому вы решили скоротать время сидя в капитанской каюте и распределяя еще не найденные сокровища.
Кроме того, за пару недель до отправления в экспедицию вы успели провести переговоры с несколькими весьма состоятельными людьми и примерно знали,
сколько сможете получить, продав им Гиперкуб.

Одним из ваших давних желаний было приобретение земли в живописном месте, где вы могли бы построить дом и разводить животных редких видов.
Подобное мероприятие требует весьма немалых денег, которые, скорее всего, появятся у вас в ближайшее время.

На входе ваша функция получит многострочную строку, состоящую из '0' и '#', где '0' обозначают пустые участки земли, а '#' - часть вашего дома.
Ваша задача - определить площадь прямоугольного участка земли, который вам необходим, чтобы его хватило для постройки дома.

Входные данные: План дома.
Выходные данные: Размер прямоугольного участка для строительства.

Пример:

house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

Как это используется: Для рационального использования ресурсов.

Предусловия:
2x2 <= размер строки <= 10x10 
"""
