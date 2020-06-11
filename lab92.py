def swap_nodes(a):
    l = []
    l2 = []
    for i in range(len(a)):
        if i%2 == 0:
            l.append(a[i])
        else:
            l2.append(a[i])
    print(l)
    print(l2)

    l3 = []
    if len(a)%2 == 0:
        for i in range(len(l2)):
            l3.append(l2[i])
            l3.append(l[i])
        print(l3)
        return l3
    else:
        for i in range(len(l2)):
            l3.append(l2[i])
            l3.append(l[i])
        l3.append(l[-1])
        print(l3)
        return l3


if __name__ == '__main__':
    #assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    #assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]

"""
Ваша задача поменять местами парные элементы списка (Iterable).
Если вам дан список из 4х элементов, то ваша функция должна вернуть такой же список,
только в нем поменяны местами первый со вторым и третий с четвертым элементы.

Если элементов не парное количество, то последний, непарный, элемент оставить на своем месте.
Пустой список должен остаться пустым.

Input: Iterable.
Output: Iterable.

Example:
swap_nodes([1, 2, 3, 4]) == [2, 1, 4, 3]
swap_nodes([5, 5, 5, 5]) == [5, 5, 5, 5]
"""
