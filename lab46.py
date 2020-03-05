from itertools import islice
from itertools import count
VOWELS = "aeiouy"
SOGLAS = "bcdfghjklmnpqrstvwxz"

def translate(phrase):
    l = []
    count = 0
    while count < (len(phrase)-2):
        if phrase[count]==phrase[count+1]==phrase[count+2] and phrase[count] in VOWELS:
            l.append(phrase[count])
            count = count + 2
        if phrase[count] in SOGLAS:
            l.append(phrase[count])
        if phrase[count] == " ":
            l.append(phrase[count])
        count = count + 1
    if phrase[-2] in SOGLAS:
        l.append(phrase[-2])
    if phrase[-1] in SOGLAS:
        l.append(phrase[-1])

    print("".join(l))

    return "".join(l)

if __name__ == '__main__':
    #assert translate("hieeelalaooo") #== "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") #== "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") #== "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") #== "sos aaa", "Mayday, mayday"



"""
У Стефана есть друг -- маленькая робо-птичка. Какое то время он пытался научить ее говорить по-английски.
И вот сегодня она произнесла первое слово: "hieeelalaooo". Звучит как "hello", но слишком уж много гласных.
Стефан попросил Николу помочь с этим, и тот изучил, как птица меняет слова.
Теперь нам осталось только написать модуль для перевода с птичьего.
Птичка меняет слова по следующим правилам:

    - после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
    - после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);

Гласные буквы == "aeiouy".

Вам дана птичья фраза как несколько слов разделеных пробелами (каждая пара слов разделена одним пробелом).
Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре.
Необходимо перевести эту птичью песню в понятную простым роботам фразу.

Входные данные: Птичья фраза как строка (string).
Выходные данные: Перевод как строка (string).

Примеры:
translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"

Связь с реальной жизнью: Этот простой "шифр" похож на тот, который используют дети для своего "птичьего" языка.
Но теперь-то вы легко взломаете их хитрости.

Предусловия: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
Фраза всегда имеет перевод.
"""

"""
    for i in range(len(phrase)-2):        
        #print(i)
        if phrase[i]==phrase[i+1]==phrase[i+2] and phrase[i] in VOWELS:
            l.append(phrase[i])
            i = i+2
            print(phrase[i])
        if phrase[i] in SOGLAS:
            l.append(phrase[i])
        if phrase[i] == " ":
            l.append(phrase[i])
    l.append(phrase[-2:-1])
    print(l)
"""
