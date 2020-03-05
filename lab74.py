from decimal import Decimal
def total_cost(calls):
    calls_list = []
    limit = 0
    over_limit = 0

    days = []
    for i in range(len(calls)):
        calls_list.append(calls[i][0:10] + ' ' + calls[i][20:])
        days.append(calls[i][0:10])
    print(set(days), 'days') # {'2014-01-03', '2014-01-01', '2014-01-02'}
    
    date_list = []
    for i in set(days): # из словаря в список
        date_list.append(i)
    print(date_list, 'date_list') # ['2014-01-03', '2014-01-01', '2014-01-02']

    empty_list = [[] for i in range(len(date_list))] # добавляем пустые списки len(date_list) раз
    empty_list_copy = [[] for i in range(len(date_list))]

    calls_list2 = []
    for i in calls_list:
        calls_list2.append(i.split(' '))
    print(calls_list2, 'calls_list2') # [['2014-01-01', '181'], ['2014-01-02', '600'], ['2014-01-03', '6009'], ['2014-01-03', '200']]

    for i in range(len(date_list)):
        for j in range(len(calls_list2)):
            if calls_list2[j][0] == date_list[i]:
                empty_list[i].append(calls_list2[j][1])
    print(empty_list, 'empty_list') # [['6009', '200'], ['181'], ['600']]

    for i in range(len(empty_list)):
        for j in empty_list[i]:           
            if int(j) % 60 != 0:
                empty_list_copy[i].append(str(int(j) // 60 + 1))
            else:
                empty_list_copy[i].append(str(int(j) // 60))
    print(empty_list_copy, 'empty_list_copy') # [['101', '4'], ['4'], ['10']]

    over_limit_time = 0
    for i in empty_list_copy: # подсчет стоимости с учетом перелемита
        time_call = sum(Decimal(j) for j in i)
        if time_call <=100:
            over_limit_time = over_limit_time + time_call
        else:
            over_limit_time = over_limit_time + 100 + (time_call - 100)*2

    print(over_limit_time,'over_limit_time')        
    return int(over_limit_time)


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    #assert total_cost(("2014-02-05 01:00:00 1",
    #                   "2014-02-05 02:00:00 1",
    #                   "2014-02-05 03:00:00 1",
    #                   "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    #assert total_cost(("2014-02-05 01:00:00 60",
    #                   "2014-02-05 02:00:00 60",
    #                   "2014-02-05 03:00:00 60",
    #                   "2014-02-05 04:00:00 6000",
    #                   "2014-02-06 01:00:00 100")) #== 106, "Precise calls"

"""
Call to Home

Николя убежден, что София звонит домой слишком много и у нее большие счета за звонки.
Он собрал счета звонков Софии за последние несколько дней и хочет посчитать сколько потратила София на разговоры.

Счет представлен в виде массива, содержащего информацию о звонках.
Помогите Николя посчитать стоимость каждого звонка Софии.
Каждый звонок представлен как строка, содержащая дату, время и длительность разговора в секундах в следующем формате:

"ГГГГ-ММ-ДД чч:мм:сс длительность"

Где дата и время - это дата и время начала звонка.

У компания "Space-Time Communications" действуют следующие тарифы:
    Первые 100 (сто) минут в день оплачиваются по тарифу 1 монета в минуту;
    После 100 минут разговора в день, каждая минута стоит 2 монеты;
    Длительность всех звонков округляется вверх до минут. Например, 59 сек ≈ 1 мин, 61 сек ≈ 2 мин;
    Звонки считаются за тот день, в котором они начались. Например, если звонок начался 2014-01-01 23:59:59, то он относится к 2014-01-01;

Например:
2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200

Первый день -- 181с≈4м -- 4 монеты;
Второй день -- 600с=10м -- 10 монет;
Третий день -- 6009с≈101м + 200с≈4м -- 100 + 5 * 2 = 110 монет;
Всего -- 124 монеты.

Входящие данные: Информация о звонках в виде кортежа(tuple) строк(strings).
Исходящие данные: Общая сумма звонков в виде целого числа(integer).

Например:
total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124


Как это можно использовать: Это задание научит работать с различными типами даты.
Иногда полная дата не нужна и нужно оперировать только с необходимыми фрагментами даты.

Предусловия: 0 < len(calls) ≤ 30
0 < call_duration ≤ 7200
Счет отсортирован по дате.
"""
