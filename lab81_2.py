import re

def checkio(text):
    money_without_text = re.findall(r'\$\S*\b', text)
    print(money_without_text, '  money_without_text')  # ['$12.345,67', '$12,345.67']
    format_money = ''
    list_money = [] # список для сконвертированной валюты
    for i in money_without_text:
        if ',' in i: # для $12.345,67
            if ',' in i and '.' not in i and i.count(',')>=2:  # для $222,100,455
                format_money = i[1:]
            else:
                i_edit = i.replace('.', ',') # 12,345,67  меняем точки на запятые
                ind = i_edit.rfind(',') # 6  индекс последней точки
                format_money = i_edit[0:ind]+ '.' + i_edit[ind+1:]
        elif '.' in i and ',' not in i:
            ind = i.rfind('.')
            if len(i[ind+1:]) == 2: # для американского варианта, когда после запятой всего 2 цифры  "$5.34"
                format_money = i
            else:
                format_money = i[1:].replace('.', ',')  # для $1.234, $5.678
        else:
            format_money = i[1:] # для  $9
        print(format_money, '  format_money')

        if '.' in format_money:
            list_money.append(format_money)      
        else:
            list_money.append("$"+format_money) # для $9 - целых чисел
    print(tuple(list_money), "  кортеж") # ('$12,345.67', '$12,345.67') приводим к кортежу       
        
    text_without_money = re.sub(r'\$\S*\b', '{}', text)  # Euro Style = {}, US Style = {}  заменяем на {} для метода .format
    print(text_without_money, '  text_without_money')   

    text_converted = text_without_money.format(*tuple(list_money)) # подставляем валюту в текст
    print(text_converted)
    print("______________")
   
    return text_converted

if __name__ == '__main__':
    assert checkio("$222,100,455") == "$222,100,455"
    assert checkio("$1.234.567,89") == "$1,234,567.89"
    assert checkio("$0,89") == "$0.89"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67"
    assert checkio("$9")
    assert checkio("$5.34") == "$5.34"
    assert checkio("$1.234, $5.678 and $9") == "$1,234, $5,678 and $9"

"""
Многие страны используют разные соглашения для разделителя тысяч и десятичного знака.
Например, в Нидерландах один миллион одна тысяча двести восемьдесят одна сотая записывается как 1.001.200,80, а в США - 1,001,200.80.
Используйте свои навыки кодирования, чтобы конвертировать доллары в первом стиле (Нидерланды, Германия, Россия,
Турция, Бразилия и другие) во второй стиль (США, Великобритания, Канада, Китай, Япония, Мексика и другие).

Следует конвертировать только суммы в долларах: от $1.234,50 до $1,234.50, от $1.000 до $1,000 и от $4,57 до $4.57.
Но не конвертируйте IP-адрес вашего маршрутизатора 192.168.1.1. Также оставьте валюту в стиле США без изменений.

Входные данные: строка, содержащая суммы в долларах для преобразования.
Вывод: строка с конвертированными валютами.
"""
