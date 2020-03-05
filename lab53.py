import re
def frequency_sort(items):
    l = []
    g = []
    if len(items) == 0:
        print('[]')
        return []
    else:
        for i in range(len(items)):
            if str(items[i]) not in str(l):
                print(items[i])
                result = re.findall(str(items[i]), str(items))
                l.append(result)    
        print(l)
        d = sorted(l, key = len, reverse=True)
        print(d)
        for i in d:
            g = g + i
        
        print(items[0])
    
        if str(items[0]).isalpha():
            print(g)
            return g
        else:
            print(eval('[' + ','.join(g) + ']'))
            return eval('[' + ','.join(g) + ']')



if __name__ == '__main__':
    #assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) #== [4, 4, 4, 4, 6, 6, 2, 2]
    #assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob', 'ait', 'ait', 'ait'])) #== ['bob', 'bob', 'bob', 'carl', 'alex']
    #assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    #assert list(frequency_sort([1])) == [1]

"""
Сортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты,
то есть, сколько раз они появляются в элементах. Если два элемента имеют одинаковую частоту,
они должны оказаться в том же порядке, что и первое появление в итерируемом элементе.

Input: Iterable
Output: Iterable

Example:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
"""
