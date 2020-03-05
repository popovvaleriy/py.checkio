import datetime
import time
def time_converter(time):    
    hour = int(time[0:2]) 
    minute = time[3:5]
    
    format = '%H:%M'
    date_formatted = datetime.datetime.strptime(time, format)
    
    
    if hour < 12:
        if hour == 0:
            print('12' + date_formatted.strftime(":" + str(minute)) + ' a.m.')
            return '12' + date_formatted.strftime(":" + str(minute)) + ' a.m.'
        if hour < 10:    
            print(date_formatted.strftime(str(hour) + ":" + str(minute)) + ' a.m.')
            return date_formatted.strftime(str(hour) + ":" + str(minute)) + ' a.m.'
    if hour >= 12:
        print(str(int(date_formatted.strftime('%I'))) + date_formatted.strftime(":" + str(minute)) + ' p.m.')
        return str(int(date_formatted.strftime('%I'))) + date_formatted.strftime(":" + str(minute)) + ' p.m.'

if __name__ == '__main__':
    assert time_converter('12:30') #== '12:30 p.m.'
    assert time_converter('09:00') #== '9:00 a.m.'
    assert time_converter('23:15') #== '11:15 p.m.'
    assert time_converter('00:00')
    assert time_converter('12:00')
    assert time_converter('18:50')

"""
Вы предпочитаете использовать 12-часовой формат времени, но современный мир живет в 24-часовом формате и вывидите это повсюду.
Ваша задача - переконвертировать время из 24-часового формата в 12-часовой, использкя следующие правила:
- выходной формат должен быть 'чч:мм a.m.' (для часов до полудня) или 'чч:мм p.m.' (для часов после полудня)
- если часы меньше 10 - не пишите '0' перед ними. Например: '9:05 a.m.'

Входные данные: Время в 24-часовом формате (как строка).
Выходные данные: Время в 12-часовом формате (как строка).

Примеры:
time_converter('12:30') == '12:30 p.m.'
time_converter('09:00') == '9:00 a.m.'
time_converter('23:15') == '11:15 p.m.'

Как это используется: Для работы с разными форматами времени.

Предусловия:
'00:00' <= время <= '23:59'
"""
