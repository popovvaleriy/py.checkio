def group_equal(els):
    if els == []:
        print("empty")
        return []

    els_list = []
    for i in range(len(els)-1):
        if els[i] == els[i + 1]:
            els_list.append(els[i])
        if els[i] != els[i + 1]:
            els_list.append(els[i])
            els_list.append('*')            
    els_list.append(els[-1])    
    print(els_list) # [1, 1, '*', 4, 4, 4, '*', 'hello', 'hello', '*', 4]

    els_list_group = [[]]
    for i in els_list:
        if i=='*':
            els_list_group.append([])
        else:
            els_list_group[-1].append(i)
    print(els_list_group) # [[1, 1], [4, 4, 4], ['hello', 'hello'], [4]]

    return els_list_group

if __name__ == '__main__':
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []

"""
Group Equal consecutive

Имея список элементов, создайте и верните список, элементы которого являются списками,
которые содержат последовательные серии одинаковых элементов исходного списка.
Обратите внимание, что элементы, которые не дублируются в исходном списке,
должны в результате стать одноэлементными списками, чтобы каждый элемент был включен в итоговый список списков.

Входные данные: Список строк (strs) и целых чисел (ints).
Выходные данные: Список списков строк (strs) и целых чисел (ints).

Пример:
group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
group_equal([1]) == [[1]]
group_equal([]) == []
"""

"""
    #test = [['4', '4', '4']]
    #test2 = [['hello', 'hello']]
    #print((',').join(test[0]))
    #print((',').join(test2[0]))
"""
