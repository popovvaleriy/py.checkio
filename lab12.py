import re
def second_index(text: str, symbol: str) -> [int, None]:
    result = re.findall(symbol, text)
    #print(result)
    if symbol in text:
        l = []
        for i, j in enumerate(text):
            if j == symbol:
                #print(i)
                l.append(i)            
        #print(l)
        if len(l) == 1:
            print('None')
            return None
        if len(l) >= 2:
            print(l[1])
            return l[1]
    else:
        print('None')
        return None


if __name__ == '__main__':
#    print('Example:')
#    print(second_index("sims", "s"))  
    assert second_index("sims", "s") #== 3, "First"
    assert second_index("find the river", "e") #== 12, "Second"
    assert second_index("hi", " ") #is None, "Third"
    assert second_index("hi mayor", " ") #is None, "Fourth"
    assert second_index("hi mr Mayor", " ") #== 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')



"""
Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims".
Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать,
что "s" – это самый первый символ в слове "sims", а значит индекс первого вхождения равен 0.
Но нам необходимо найти вторую "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.

Input: Две строки (String).
Output: Int or None

Примеры:

second_index("sims", "s") == 3
second_index("find the river", "e") == 12
second_index("hi", " ") is None
"""
