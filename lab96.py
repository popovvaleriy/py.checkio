def words_order(text: str, words: list) -> bool:
    index_text = []
    index_words = []
    words_check = []
    
    for i in words:
        if i in words_check:
            print(False, "  Element duplication")
            return False
        else:
            words_check.append(i)
        index_text.append([i, words.index(i)])
        if i not in index_words:
            if i not in text.split(" "):
                print(False, "  No Element in text")
                return False
            else:
                index_words.append([i, text.split(" ").index(i)])
        
    index_text = sorted(index_text, key=lambda x: x[1])
    index_words = sorted(index_words, key=lambda x: x[1]) # сортровка списка по числу
    print(index_text, "  index_text")
    print(index_words, "  index_words")

    for i in range(len(index_text)): # перебираем паралельно два списка и проверяем, одинаковы ли элементы 
        #print(index_text[i][0], "  i[0] *")
        #print(index_words[i][0], "  j[0] *")
        #print("____")
        if index_text[i][0] == index_words[i][0]:
            continue
        else:
            print(False)
            return False
    print(True)
    return True


if __name__ == '__main__':
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here', ['world', 'im', 'here']) == True 
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world', 'here', 'hi']) == False
    assert words_order('hi world im here', ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here', ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False


"""
У вас есть текст и список слов. Вам необходимо проверить,
отображаются ли слова в списке в том же порядке, что и в данном тексте.

Случаи, которые вы должны ожидать при решении этой задачи:
     - слова из списка нет в тексте - ваша функция должна возвращать False;
     - любое слово может встречаться в тексте более одного раза - используйте только первое;
     - два слова в данном списке одинаковы - ваша функция должна возвращать False;
     - условие чувствительно к регистру, что означает «привет» и «привет» - два разных слова;
     - текст включает только английские буквы и пробелы.

Вход: два аргумента. Первый - это заданный текст, второй - список слов.
Выход: бул.

Example:

words_order('hi world im here', ['world', 'here']) == True
words_order('hi world im here', ['here', 'world']) == False
words_order('hi world im here', ['world']) == True

words_order('hi world im here',
 ['world', 'here', 'hi']) == False
 
words_order('hi world im here',
 ['world', 'im', 'here']) == True
 
words_order('hi world im here',
 ['world', 'hi', 'here']) == False
 
words_order('hi world im here', ['world', 'world']) == False
words_order('hi world im here',
 ['country', 'world']) == False
 
words_order('hi world im here', ['wo', 'rld']) == False
words_order('', ['world', 'here']) == False

"""
