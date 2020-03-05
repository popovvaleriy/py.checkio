import locale
import re

def checkio(text):
    money_without_text = re.findall(r'\$\S*\b', text)
    print(money_without_text, '  money_without_text')  # ['$12.345,67', '$12,345.67']
    format_money = ''
    list_money = [] # список для конвертированной валюты
    for i in money_without_text:
        if ',' in i: # для $12.345,67
            print(i, "  i")
            i_edit = i[1:].replace(',', '.') # 12.345.67  убираем запятые
            ind = i_edit.rfind('.')
            #print(ind, '  ind') # 6  индекс последней точки
            format_money = i_edit[0:ind].replace('.', '') + '.' + i_edit[ind+1:]
        elif '.' in i and ',' not in i:
            format_money = i[1:].replace('.', ',')  # для $1.234, $5.678
        else:
            format_money = i[1:] # для  $9
        print(format_money, '  format_money')  # 12345.67 приводим к виду для конвертации методом local

        if '.' in format_money:
            locale.setlocale(locale.LC_ALL, 'English_United States.1252')
            conv = locale.localeconv()        
            locale.format_string("%d", float(format_money), grouping=True)
            money_converted = locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], float(format_money)), grouping=True)
            print(money_converted,'  resul4')  #$12,345.67  сконвертированная валюта
            list_money.append(money_converted)
        else:
            list_money.append("$"+format_money) # для $9 - целых чисел
    print(tuple(list_money), "  кортеж") # ('$12,345.67', '$12,345.67') приводим к кортежу
       
        
    text_without_money = re.sub(r'\$\S*\b', '{}', text)  # Euro Style = {}, US Style = {}  заменяем на {} для метода .format
    print(text_without_money, '  result3')   

    text_converted = text_without_money.format(*tuple(list_money)) # подставляем валюту в текст
    print(text_converted)
    print("______________")

    
    return text_converted

if __name__ == '__main__':    
    assert checkio("$1.234.567,89") == "$1,234,567.89"
    assert checkio("$0,89") == "$0.89"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67"
    assert checkio("$9")
    assert checkio("$1.234, $5.678 and $9") == "$1,234, $5,678 and $9"

"""
    #locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    #conv = locale.localeconv()  # get a mapping of conventions
    #x = 1234567.8
    #locale.format("%d", x, grouping=True)  #'1,234,567'
    #result = locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)
    #print(result)

Многие страны используют разные соглашения для разделителя тысяч и десятичного знака.
Например, в Нидерландах один миллион одна тысяча двести восемьдесят одна сотая записывается как 1.001.200,80, а в США - 1,001,200.80.
Используйте свои навыки кодирования, чтобы конвертировать доллары в первом стиле (Нидерланды, Германия, Россия,
Турция, Бразилия и другие) во второй стиль (США, Великобритания, Канада, Китай, Япония, Мексика и другие).

Следует конвертировать только суммы в долларах: от $1.234,50 до $1,234.50, от $1.000 до $1,000 и от $4,57 до $4.57.
Но не конвертируйте IP-адрес вашего маршрутизатора 192.168.1.1. Также оставьте валюту в стиле США без изменений.

Входные данные: строка, содержащая суммы в долларах для преобразования.
Вывод: строка с конвертированными валютами.
"""
