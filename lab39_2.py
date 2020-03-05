import re
import datetime
import time
def time_converter(time):
  
    a_m = 'a.m.'
    p_m = 'p.m.'

# Чтобы получить объект datetime из строки, используйте datetime.datetime.strptime:

    if a_m in time:
        if len(time) == 9:           
            no_text = re.findall(r'\d:\d\d', time) # ['9:00']
            my_time = datetime.time(hour=int(no_text[0][0]), minute=int(no_text[0][2:]))            
            print(my_time.strftime("%H:%M")) # 09:00
            return my_time.strftime("%H:%M")
        if len(time) == 10:           
            no_text = re.findall(r'\d\d:\d\d', time) # ['9:00']
            my_time = datetime.time(hour=int(no_text[0][:2]), minute=int(no_text[0][3:]))            
            print(my_time.strftime("%H:%M")) # 09:00
            return my_time.strftime("%H:%M")        
           
    if p_m in time:
        if len(time) == 9:
            no_text = re.findall(r'\d:\d\d', time) # ['9:00']
            hour24 = int(no_text[0][0]) + 12 #21
            my_time = datetime.time(hour=int(hour24), minute=int(no_text[0][2:]))
            print(my_time.strftime("%H:%M")) # 21:00
            return my_time.strftime("%H:%M")
        if len(time) == 10:            
            no_text = re.findall(r'\d\d:\d\d', time)
            if int(no_text[0][:2]) == 12:
                my_time = datetime.time(hour=int(no_text[0][:2]), minute=int(no_text[0][3:]))
                print(my_time.strftime("%H:%M"))
                return my_time.strftime("%H:%M")
            else:
                hour24 = int(no_text[0][:2]) + 12
                my_time = datetime.time(hour=int(hour24), minute=int(no_text[0][3:]))
                print(my_time.strftime("%H:%M"))
                return my_time.strftime("%H:%M")


if __name__ == '__main__':
    assert time_converter('00:30 a.m.') #== '00:30'
    assert time_converter('12:30 a.m.') #== '12:30'
    assert time_converter('12:30 p.m.') #== '12:30'
    assert time_converter('9:00 a.m.') #== '09:00'
    assert time_converter('11:15 p.m.') #== '23:15'
    assert time_converter('11:15 a.m.') #== '11:15'
    assert time_converter('9:00 p.m.') #== '21:00'

"""
# https://www.w3schools.com/python/python_datetime.asp
Вы современый человек, предпочитающий использовать 24-часовой формат времени.
Но в некоторых регионах используют 12-часовой формат. Ваша задача - переконвертировать
время из 12-часового формата в 24-часовой, используя следующие правила:
- выходной формат должен быть 'чч:мм'
- если часы меньше 10 - допишите '0' перед ними. Например: '09:05'

Входные данные: Время в 12-часовом формате (как строка).
Выходные данные: Время в 24-часовом формате (как строка).

Примеры:
time_converter('12:30 p.m.') == '12:30'
time_converter('9:00 a.m.') == '09:00'
time_converter('11:15 p.m.') == '23:15'

Как это используется: Для работы с разными форматами времени.
Предусловия:
'00:00' <= время <= '23:59'
"""
