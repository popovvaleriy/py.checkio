import re
markers = ("help", "asap", "urgent")

def is_stressful(subj):
    if subj.rfind("!!!"): 
        if subj[-4:-1] == "!!!":  # поиск знаков воскл. с конца списка
            print(True)
            return True    
    l = []    
    f = []
    for i in range(len(subj)-1):  # отсеиваем повторяющиеся буквы
        if subj[i] != subj[i+1]:
            f.append(subj[i])
    f.append(subj[-1]) # добавляем последний символ т.к. цикл работает до len(subj)-1
    print(f)  # ['H', 'e', 'y', '!', ' ', 'I', '’', 'm', ' ', 'h', 'a', 'v', 'i', 'n', 'g', ' ', 's', 'o', ' ', 'm', 'u', 'c', 'h', ' ', 'f', 'u', 'n', '!', '”']
    result3 = (','.join(f)).replace(",", "")    
    print(result3)

    if result3.isupper(): # Если все буквы заглавные
        return True
    else:
        result = (re.sub(r'[! -.\s]', '', result3)).lower()  # убираем спец. символы
        for i in markers:
            if re.search(i, result):
                l.append("Tr")
        if 'Tr' in l:
            return True
        else:
            return False


if __name__ == '__main__':
    assert is_stressful("where are you?!!!!") == True
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") == False
    assert is_stressful("something is gona happen") == False
    assert is_stressful("UUUURGGGEEEEENT here") == True
    assert is_stressful("Hi") == False
    assert is_stressful("I neeed HELP asap") == True
    assert is_stressful("HELP") == True
    assert is_stressful("I neeed HELP") == True
    assert is_stressful("I neeed HELP!!!!") == True
    assert is_stressful("We need you A.S.A.P.!!") == True

"""
У Софии был очень напряженный месяц и она решила взять отпуск на неделю.
Чтобы избежать стресса во время отпуска, она хочет перенаправлять Стивену электронные письма со стрессовыми темами.

Функция должна распознавать является ли тема письма стрессовой.
Стрессовая тема определяется тем, что все буквы в верхнем регистре,
и / или заканчиваются как минимум тремя восклицательными знаками,
и / или содержат по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent".
Любое из этих слов-маркеров может быть написано по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P»,
и даже очень непринужденно «HHHEEEEEEEEELLP».

Входные данные: Тема письма в виде строки.
Выходные данные: Boolean.

Пример:

is_stressful("Hi") == False
is_stressful("I neeed HELP") == True

Предварительное условие: Тема может содержать до 100 букв.
"""


"""    
    if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in subj):
        if result3.isupper():
            print(True)
            return True
        else:
            result = (re.sub(r'[! -.\s]', '', result3)).lower()
            for i in markers:
                if re.search(i, result):
                    l.append("Tr")
            print(l)
            if 'Tr' in l:
                print(True)
                return True
            else:
                print(False)
                return False


    #result = (re.sub(r'[”! -.\s]', '', subj)).lower()
    #print(result)
"""
