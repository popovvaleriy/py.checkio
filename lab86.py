from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:

    l = []
    m = 0
    n = size
    for i in items:
        if items[m:n] != []:
            l.append(items[m:n])
        m +=size
        n +=size
    print(l)
    return l


if __name__ == '__main__':
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]


"""
У вас много работы, поэтому вы можете разделить ее на более мелкие части.
Таким образом, вы будете знать, что вы будете делать в понедельник, во вторник и так далее.

Разделите список на более мелкие списки одинакового размера (куски).
Последний блок может быть меньше размера блока по умолчанию.
Если список пуст, то у вас вообще не должно быть фрагментов.

Вход: два аргумента. Список и размер куска.
Вывод: Iterable с чанкованным Iterable.


You have a lot of work to do, so you might want to split it into smaller pieces.
This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

Spit a list into smaller lists of the same size (chunks).
The last chunk can be smaller than the default chunk-size.
If the list is empty, then you shouldn't have any chunks at all.

Input: Two arguments. A List and chunk size.
Output: An Iterable with chunked Iterable.

Example:
chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
chunking_by([3, 4, 5], 1) == [[3], [4], [5]]

Precondition: chunk-size > 0 
"""
