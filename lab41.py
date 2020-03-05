import datetime
import time
def date_time(time: str) -> str:
    day = int(time[0:2]) #20
    hour = int(time[11:13]) #3
    minute = int(time[14:]) #5
    format = '%d.%m.%Y %H:%M'    
    date_formatted = datetime.datetime.strptime(time, format)
    if hour == minute == 1:
        print(date_formatted.strftime(str(day) + " %B %Y year " + str(hour) + " hour " + str(minute) + " minute"))
        return date_formatted.strftime(str(day) + " %B %Y year " + str(hour) + " hour " + str(minute) + " minute")
    else:
        print(date_formatted.strftime(str(day) + " %B %Y year " + str(hour) + " hours " + str(minute) + " minutes"))    
        return date_formatted.strftime(str(day) + " %B %Y year " + str(hour) + " hours " + str(minute) + " minutes")

if __name__ == '__main__':

    assert date_time("01.01.2000 00:00") #== "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") #== "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") #== "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    assert date_time("20.11.1990 03:05")
    assert date_time("09.07.1995 16:50")
    assert date_time("01.01.2000 00:00")
    assert date_time("11.04.1812 01:01") #== "11 April 1812 year 1 hour 1 minute"

"""
Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.

Входные данные: Дата и время как строка, состоящая из чисел (например: 14.02.2018 16:55)
Выходные данные: Та же самая дата и время, но в более развернутом формате

Пример:
date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"

Обратите внимание, что слова "hour" и "minute" (в единственном числе) используются
только когда время 01:mm (1 hour) или hh:01 (1 minute).

Во всех остальных случаях следует использовать "hours" и "minutes".
Для названий месяцев и остальных слов следует использовать их английские эквиваленты -

January, February, March, April, May, June, July,
August, September, October, November, December;
year, hour/hours, minute/minutes

Как это используется: Для улучшения взаимопонимания между человеком и компьютером.

Предусловия:
0 < date <= 31
0 < month <= 12
0 < year <= 3000
0 < hours < 24
0 < minutes < 60
"""
