from collections import Counter
import re
text = 'When I was One I had just begun When I was Two I was nearly new'
words = ['i', 'was', 'three', 'near']

def popular_words(text: str, words: list) -> dict:
    text2 = text.casefold().split()
    #print(text2) # ['when', 'i', 'was', 'one', 'i', 'had', 'just', 'begun', 'when', 'i', 'was', 'two', 'i', 'was', 'nearly', 'new']
    dictionary = {}
    overlap_in_text = []
    words_in_text = []
    for z in text2:
        result = words.count(z)
        #print(z, result)
        result_list = (z + ":" + str(result)).split(':')
        #print(result_list)
        result2 = overlap_in_text.append(result_list)
    #print(r)
#[['when', '0'], ['i', '1'], ['was', '1'], ['one', '0'], ['i', '1'], ['had', '0'], ['just', '0'], ['begun', '0'],
#['when', '0'], ['i', '1'], ['was', '1'], ['two', '0'], ['i', '1'], ['was', '1'], ['nearly', '0'], ['new', '0']]
    for i in overlap_in_text:
        if i[0] in words:
            result3 = words_in_text.append(i)
            for z in words_in_text:
                word_count = words_in_text.count(i)
            dictionary.update({str(i[0]):word_count})
    #print(m) #[['i', '1'], ['was', '1'], ['i', '1'], ['i', '1'], ['was', '1'], ['i', '1'], ['was', '1']]
    #print(dictionary) #{'i': 4, 'was': 3}
    #print(dictionary.keys()) #dict_keys(['i', 'was'])
    for i in words:
        if i in dictionary.keys():
            None
        else:
            dictionary.update({str(i):0})

    print(dictionary)
    return dictionary

popular_words(text, words)

"""
if __name__ == '__main__':
#    print("Example:")
#    print(popular_words('''
#When I was One
#I had just begun
#When I was Two
#I was nearly new
#''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")


Ваша задача в этой миссии определить популярность определенных слов в тексте.
На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.

При решении этой задачи обратите внимание на следующие моменты
    Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one",
    значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
    Искомые слова всегда указаны в нижнем регистре
    Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)

Входные параметры: Текст и массив искомых слов.
Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то,
сколько раз они встречаются в исходном тексте.

Пример:

popular_words('''

When I was One
I had just begun
When I was Two
I was nearly new

''', ['i', 'was', 'three', 'near']) == {

    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
    }

Предусловия:
Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.


"""
