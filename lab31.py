def sun_angle(time):
    time_min = time.split(':')  #['07', '00']
    print(time_min)
    print(int(time_min[0]))  #7
    time_hour = int(time_min[0])
    time_minut = int(time_min[1])
    time_min_summ = time_hour*60 + time_minut
    print(time_min_summ)

    if time_min_summ < 360 or time_min_summ > 1080:
        print("I don't see the sun!")
        return "I don't see the sun!"
    if time_min_summ == 360:
        print("0")
        return 0    
    if time_min_summ == 1080:
        print("180")
        return 180         
    else:
        if time_hour <= 12:        
            degrees = ((time_hour-6)*60 + time_minut)*0.25
            print(degrees)
            return degrees
        if time_hour > 12:
            degrees = ((18 - time_hour)*60 + time_minut)*0.25
            print(degrees)
            return degrees
        

if __name__ == '__main__':
    assert sun_angle("18:01")
    assert sun_angle("5:00")
    assert sun_angle("07:00") == 15
    assert sun_angle("14:00")
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""
Любой настоящий путешественник должен уметь делать три вещи: добывать огонь,
находить воду и извлекать полезную информацию из природы, окружающей его.
Программирование не поможет вам с огнем и водой, но с добычей информации справится вполне.

Ваша задача - определить угол солнца над горизонтом, зная время суток.
Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов.
В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".


Входные данные: Время.
Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой.

Пример:
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"

Как это используется: Жизненно необходимый навык для любого путешественника,
особенно в случае утери компаса и разрядившегося мобильного телефона с GPS.
Правда, в такой ситуации приходится решать обратную задачу - определять время по углу солнца и производить несколько дополнительных расчетов.

Предусловия:
00:00 <= время <= 23:59
"""
