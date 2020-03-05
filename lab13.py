import re

def between_markers(text: str, begin: str, end: str) -> str:
    g = (begin, end)
    for i in g:
        if begin and end in text and text.find(begin) > text.find(end):
            print("Wrong direction")
            return ''
        if g[0] in text and g[1] not in text:
            temp = text.find(begin)
            print(temp)
            result = text.split(begin, 1)[1]
            print(result)
            return result
        if g[0] not in text and g[1] in text:
            temp = text.find(end)
            result = text.split(end, 1)[0] # (end, 1) 1 - количество сработок
            print(result)
            return result
        if g[0] and g[1] in text:       
            result = re.split(begin, text)
            print(result)
            result2 = re.split(end, result[1])  #Этот метод разделяет строку по заданному шаблону.
            print(result2)
            print(result2[0])            
            return result2[0]
        if g[0] and g[1] not in text:
            print(text)
            return text

if __name__ == '__main__':
    #print('Example:')
    #print(between_markers('What is >apple<', '>', '<'))
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') #== "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") # == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') #== 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
    #assert between_markers('No <hi>', '>', '<')  #== '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

"""
print('dsadfdsf/njkvnsaasda/uuuuu'.split('/',2)[1:])  2 - количество сработок
"""

"""
Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:

    Начальный и конечный маркеры всегда разные
    Если нет начального маркера, то началом считать начало строки
    Если нет конечного маркера, то концом считать конец строки
    Если нет ни конечно ни начального маркеров, то просто вернуть всю строку
    Если конечный маркер стоит перед начального, то вернуть пустую строку

Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.

Примеры:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'

Как это использутеся: может использоваться для парсинга небольшой верстки
Предусловия: не может быть более одного маркера одного типа
"""
