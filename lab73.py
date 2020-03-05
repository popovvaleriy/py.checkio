def between_markers(text: str, begin: str, end: str) -> str:
    print(text.index(begin))
    print(text.rindex(end))
    print(text[text.index(begin)+1:text.rindex(end)])
    return text[text.index(begin)+1:text.rindex(end)]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"

"""
Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами.
Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers.

    Начальный и конечный маркеры всегда разные.
    Начальный и конечный маркеры всегда размером в один символ.
    Начальный и конечный маркеры всегда есть в строке и идут один за другим.

Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.

Пример:
between_markers('What is >apple<', '>', '<') == 'apple'


Как это используется: Может использоваться для парсинга небольшой верстки.
Предусловия: Не может быть более одного маркера одного типа.
"""
