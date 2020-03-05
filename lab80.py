from collections import Counter

def most_wanted(text: str) -> str:
    #''.join(filter(str.isalpha, text))  #удалить все символы, кроме букв
    list_words = ''.join(filter(str.isalpha, text)).lower()
    print(list_words)
    
    letter_count = Counter(list_words).most_common()
    print(letter_count, "  letter_count")  # список кортежей, список букв и их количество [('l', 3), ('o', 2), ('h', 1), ('e', 1), ('w', 1), ('r', 1), ('d', 1)]
    
    d = dict(letter_count) # перевод в словарь {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
    print(d)
    

    max_val = max(d.values())  # максимальное значение в словаре
    print(max_val, '  max_val')

    print(sorted([key for key, value in d.items() if value == max_val]), '  finish')  # вывод ключей с значением max_val

    return sorted([key for key, value in d.items() if value == max_val])

if __name__ == '__main__':
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."

"""
Most Wanted Letter

Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a".
Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой, верните список со всеми этими буквами.
Для примера, в тексте "Hello, Evan" буквы "e" и "l" встречаются по 2 раза, так что ответом будет ["e", "l"].

Вх. данные: Текст для анализа, как строка.
Вых. данные: Список наиболее частых букв.

Примеры:
most_wanted("Hello World!") == ["l"]
most_wanted("How do you do?") == ["o"]
most_wanted("One") == ["o", "n", "e"]
most_wanted("Oops!") == ["o"]
most_wanted("AAaooo!!!!") == ["a", "o"]
most_wanted("abe") == ["a", "b", "e"]

Как это используется: Для большинства задач по дешифрованию необходимо знать частоту появления различных букв в подобном тексте.
Для примера, мы легко можем взломать одноалфавитный шифр подстановки, если мы знаем вероятность появления букв.
Это также может быть полезной информацией для лингвистов.

Предусловия:
text содержит только ASCII символы.
0 < len(text) ≤ 105 
"""
