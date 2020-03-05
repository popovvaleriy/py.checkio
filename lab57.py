colors = ['Green', 'Red', 'Blue', 'Yellow']
 
class Lamp:
    def __init__(self):
        self.counter = 0

    def light(self):
        if self.counter == 4:
            self.counter = 0
            color=colors[self.counter]
        else:
            color=colors[self.counter]
            self.counter = self.counter + 1
        print(color)
        return color
    

if __name__ == '__main__':
    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"

"""
Приближаются новогодние праздники и вы решили украсить свое жилище.
Но за долгие годы обычные гирлянды и елочные игрушки вам наскучили, так что вы решили применить свои навыки программирования,
чтобы сделать нечто по-настоящему оригинальное. Ваша задача - реализовать класс Lamp() (лампочка) и метод light(),
который будет заставлять лампочку загораться очередным цветом в последовательности (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’) при каждом включении.
Если в данный момент цвет лампочки - Yellow, то при следующем включении она загорится зеленым (Green) и так далее.
В этой миссии вам может помочь такой шаблон проектирования, как State.
Он полезен в ситуациях, когда объект должен менять свое поведение в зависмости от внутреннего состояния.

Примеры:

lamp_1 = Lamp()
lamp_2 = Lamp()

lamp_1.light() #Green
lamp_1.light() #Red
lamp_2.light() #Green
   
lamp_1.light() == "Blue"
lamp_1.light() == "Yellow"
lamp_1.light() == "Green"
lamp_2.light() == "Red"
lamp_2.light() == "Blue"

Входные данные: несколько строк, указывающих на количество включений лампочки.
Выходные данные: цвет, которым светит лампочка в итоге.

Как это используется: Для реализации объектов с изменяемым поведением.
Предусловие: 4 цвета: Green, Red, Blue, Yellow.
"""
