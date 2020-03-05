import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    text2 = re.findall(r"[\w']+", text.lower()) #['a', 'quantity', 'of', 'striped', 'words']
    text_more = []
    for i in text2:
        if len(i) > 1:
            text_more.append(i)
    print(text_more) #['quantity', 'of', 'striped', 'words']

    text_more3 = []
    
    for z in text_more:
        print(z)
        text_more2 = []
        ran = range(len(z) -1)        
        if z[0] in CONSONANTS.lower():
            for i in ran:
                if z[i] in CONSONANTS.lower() and z[i + 1] in VOWELS.lower():
                    text_more2.append(z[i]+z[i + 1])
            if z[-2] in CONSONANTS.lower() and z[-1] in VOWELS.lower() and len(z)%2 != 0: #добавление последнего символа если длина слова не кратна 2м и символ и последующий символ гласный/согласный
                text_more2.append(z[-1])
            if z[-2] in VOWELS.lower() and z[-1] in CONSONANTS.lower() and len(z)%2 != 0:
                text_more2.append(z[-1])                            
        if z[0] in VOWELS.lower():
            for i in ran:
                if z[i] in VOWELS.lower() and z[i + 1] in CONSONANTS.lower():
                    text_more2.append(z[i]+z[i + 1])
            if z[-2] in CONSONANTS.lower() and z[-1] in VOWELS.lower() and len(z)%2 != 0:
                text_more2.append(z[-1])
            if z[-2] in VOWELS.lower() and z[-1] in CONSONANTS.lower() and len(z)%2 != 0:
                text_more2.append(z[-1]) 
        print(text_more2) #bird -> ['bi'] -> сверяет с словом, получаем False
        
        text3 = ','.join(text_more2)
        text4 = text3.replace(',', '')
        print(text4) #qutity
        print(z) #quantity
        if text4 == z:
            print('True')
            text_more3.append('True')
        else:
            print('False')
            text_more3.append('False')        
    print(text_more3)
    count_word = text_more3.count("True")
    print(count_word)
    return count_word

if __name__ == '__main__':
    assert checkio("For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.") # == 6
    #assert checkio("My name is ...") # == 3, "All words are striped"
    #assert checkio("Hello world") # == 0, "No one"
    #assert checkio("A quantity of striped words.") # == 1, "Only of"
    #assert checkio("Dog,cat,mouse,bird.Human.") # == 3, "Dog, cat and human"

"""
Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в лингвистике.
Сейчас они изучают английский алфавит и что с этим делать.

Алфавит разделен на гласные и согласные буквы (Да, мы разделили буквы, а не звуки).
Гласные -- A E I O U Y
Согласные -- B C D F G H J K L M N P Q R S T V W X Z

Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации.
Числа не считаются за слова (также как и смесь букв и цифр).
Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными (полосатые слова),
о есть в таких словах нет двух гласных или двух согласных букв подряд.
Слова состоящие из одной буквы - не "полосатые" (не считайте их). Регистр букв не имеет значения.

Входные данные: Текст, как строка (str).
Выходные данные: Количество "полосатых" слов, как целое число (int).

Примеры:
checkio("My name is ...") == 3
checkio("Hello world") == 0
checkio("A quantity of striped words.") == 1, "Only of"
checkio("Dog,cat,mouse,bird.Human.") == 3

Зачем это нужно: Концепции используемые в данной задаче могут быть полезным упражнением для лингвистического анализа.
Обработка текста - это очень важный инструмент для анализа книг и языков.

Предусловия:Текст содержит только ASCII символы.
0 < len(text) < 105
"""

"""
    text_more2 = []
    for i in range(len(t)):
        if t[i] in CONSONANTS.lower() and t[i + 1] in VOWELS.lower():
            #print(t[i])
            #print(t[i + 1])
            text_more2.append(t[i]+t[i + 1])
    #print(text_more2) #['qu', 'ti', 'ty']
    text3 = ','.join(text_more2)
    text4 = text3.replace(',', '')
    print(text4) #qutity
    print(t) #quantity
    if text4 == t:
        print('True')
    else:
        print('False')
"""
"""
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

for 
music 
uses 
same 
vocabulary 
in 


etc
and
"""
