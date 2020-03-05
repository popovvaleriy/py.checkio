def checkio(first, second):
    first_len = len(first)
    second_len = len(second)

    first_w = first.split(',') # ['one', 'two', 'three']
    second_w = second.split(',') # ['four', 'five', 'one', 'two', 'six', 'three']
    print(first_w)
    print(second_w)
    l = []
    if first_len >= second_len:
        for i in first_w:
            if i in second_w:
                l.append(i)
    else:
        for i in second_w:
            if i in first_w:
                l.append(i)
    l.sort() # ['one', 'three', 'two']           
    print(l)
    if len(l) > 0:
        result = ",".join(str(x) for x in l)
        print(result) # one,three,two
        return result
    else:
        return ""

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"


"""
Common Words
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми.
Попробуйте найти что общего между этими строками. Слова внутри каждой строки не повторяются.

Ваша функция должна находить все слова, которые появляются в обеих строках.
Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).
Вых. данные: Общие слова как строка (str).

Примеры:
checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

Как это используется: В этой задаче вы попрактикуетесь в работе с наборами и строками. И эти навыки будут полезными для лингвистического анализа.

Предусловия:
Каждая строка содержит не более 10 слов.
Все слова разделены запятыми.
Все слова состоят только из латинских букв в нижнем регистре.
"""
