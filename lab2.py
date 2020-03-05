import re
from collections import Counter
import string

#spisok = '1 2 3 2 1'
spisok = [1, 2, 3, 2, 1]                            

def checkio(spisok):
    #result = re.findall(r'\w', spisok)
    #print(result)
    l = []
    #f = []
    s = []
    for m in spisok:
        if spisok.count(m) > 1:
            l.append(m) #выводим элементы количество которых больше одного
    print(l)
    return l

    """
    for i in enumerate(l): #получаем индексы элементов из списка
        f.append(i)
        print(i)
    print(f) #вывод списка с индексами [(0, '1'), (1, '2'), (2, '2'), (3, '1')]
    print(f[3])
    dictionary = dict(f) #перевод списка в словарь {0: '1', 1: '2', 2: '2', 3: '1'}
    print(dictionary)
    print(dictionary.values())

    for val in dictionary.values():
        s.append(val)
    print(s)
    return s
    """
checkio(spisok)

"""
Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:

line = 'asdf fjdk;afed,fjek,asdf,foo'
result = re.sub(r'[;,\s]',' ', line)
print result

Результат:
asdf fjdk afed fjek asdf foo
"""
"""
li = ['9999999999', '999999-999', '99999x9999']

for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:   # {1} - количество вхождений
        print 'yes'
    else:
        print 'no'

Результат:
yes
no
no

"""


"""
def checkio(spisok):
    dictionary = {}
    result = sorted(re.findall(r'\w', spisok.lower()))
    print(result)
    for t in result:
        dictionary[t] = result.count(t)
        print(dictionary[t])
    print(dictionary.items())
    print(dictionary.keys())
    print(dictionary.values())
    cont = max(dictionary.values())
    print(cont)
    
    l = []
    for key in dictionary:
        if dictionary[key] == cont:
            l.append(key)
    print(l)
    
    l = sorted(l)
    print(l[0])
    return(l[0])

checkio('Lorem ipsum dolor sit amet')
"""
