def left_join(phrases):
    text = str(phrases)
    l = []

    for i in phrases:
        #print(i)
        l.append(i)
    print(l)  # ['left', 'right', 'left', 'stop']
    result2 = ','.join(l)
    print(result2) # left,right,left,stop
    result3 = result2.replace("right",'left')
    print(result3)  # left,left,left,stop
    return result3


if __name__ == '__main__':
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    #assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    #assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    #assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"

"""
Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания инструкции по обходу корабля.
Но робот был левша и зачастую шутил и запутывал своих друзей правшей.

Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
даже если это часть другого слова. Все строки даны в нижнем регистре.

Входные данные: Последовательность строк, как кортеж строк (юникод).
Выходные данные: Текст, как строка.

Пример:
left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"

Как это используется: Это просто пример операций, использующих строки и последовательности.

Предусловие:
0 < len(phrases) < 42
"""
