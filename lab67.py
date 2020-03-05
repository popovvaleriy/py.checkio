import copy

class Text:
    def __init__(self):
        self.text = ''
        self.font = ''

    def set_font(self, font):
        self.font = font

    def write(self, text):
        self.text += text

    def restore(self, text):
        self.text = text.text
        self.font = text.font

    def show(self):
        if (self.font != ''):
            font = '[' + self.font + ']'
        else:
            font = ''
        return '{}{}{}'.format(font, self.text, font)


class SavedText:
    def __init__(self):
        self.texts = {}
        self.last_version = 0

    def save_text(self, text):
        self.texts[self.last_version] = copy.copy(text)
        self.last_version += 1

    def get_version(self, version):
        return self.texts[version]


if __name__ == '__main__':
    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "


"""
Я думаю, многие из вас сталкивались с такой проблемой: работаешь в текстовом редакторе, сохраняешь документ и закрываешь редактор.
А на следующий день перечитываешь текст и понимаешь, что одна из предыдущих версий была лучше, но вернуть её уже никак нельзя.
С этой проблемой прекрасно справляются системы контроля версий (например, git), но в основном ими пользуются разработчики,
а не обычные люди, работающие с текстом.
В этой миссии вы поможете этим людям, создав прототип текстового редактора с возможностью сохранять различные версии текста,
а затем возвращаться к любой из них.
Ваша задача - реализовать 2 класса: Text и SavedText.
Первый будет отвечать за работу с текстом (добавление, изменение шрифта и т.д.), а второй - за сохранение и управление версиями.

Класс Text должен иметь следующие методы:
write(text) - добавляет указанный текст к текущему.
set_font(font name) - устанавливает шрифт текста. Шрифт распространяется на весь текст,
даже добавленный после установки шрифта и отображается в квадратных скобках перед началом текста и после конца: "[Arial]...example...[Arial]".
Шрифт может быть задан сколько угодно раз, но отображается только последний из них.
show() - отображает текущий текст и шрифт (если задан).
restore(SavedText.get_version(number)) - возвращает текст к указанной версии.

Класс SavedText должен иметь следующие методы:
save_text(Text) - сохраняет текущее состояние текста и текущий шрифт. Первая сохраненная версия имеет номер 0, вторая - 1 и так далее.
get_version(number) - метод используется вместе с методом restore класса Text и служит для выбора нужной версии текста.

В этой миссии вам может помочь такой шаблон проектирования, как Memento.

Пример:
text = Text()
saver = SavedText()
    
text.write("At the very beginning ")
saver.save_text(text)
text.set_font("Arial")
saver.save_text(text)
text.write("there was nothing.")
text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
text.restore(saver.get_version(0))
text.show() == "At the very beginning "

Входные данные: информация о тексте и о сохранениях.
Выходные данные: текст после всех команд.
Предусловие: Не более 10 запомненных состояний. 
"""
