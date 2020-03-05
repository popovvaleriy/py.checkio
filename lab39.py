import re
def time_converter(time):
    a_m = 'a.m.'
    p_m = 'p.m.'
    tw = '12:'
    a_m_hour = ['1','2','3','4','5','6','7','8','9','10','11']
    p_m_hour = ['13','14','15','16','17','18','19','20','21','22','23']
    
    time2 = []
    if a_m in time:
        if len(time) == 9:            
            no_text = re.findall(r'\d:\d\d', time) # ['9:00']
            time2.append('0')
            time2.append(no_text[0])
            # time2 = ['0', '9:00']
            result = ','.join(time2)
            result2 = result.replace(",", "")
            print(result2) # 09:00
            return result2
        if len(time) == 10:
            no_text = re.findall(r'\d\d:\d\d', time)
            #print(no_text[0][:2])
            if tw in time:
                time2.append('00')
                time2.append(no_text[0][2:])
                result = ','.join(time2)
                result2 = result.replace(",", "")
                print(result2)
                return result2
            else:
                elem = no_text[0][:2]
                time2.append(elem)
                time2.append(no_text[0][2:])            
                result = ','.join(time2) # 21,:00
                result2 = result.replace(",", "") # 21:00
                print(result2)
                return result2
            
    if p_m in time:
        if len(time) == 9:            
            no_text = re.findall(r'\d:\d\d', time) # ['9:00']
            elem = no_text[0][0]
            index = a_m_hour.index(elem) # индекс 8 цифры 9
            p_a_repl = p_m_hour[index] # 21
            time2.append(p_a_repl)
            time2.append(no_text[0][1:])            
            #print(time2) ['21', ':00']
            result = ','.join(time2) # 21,:00
            result2 = result.replace(",", "") # 21:00
            print(result2)
            return result2
        if len(time) == 10:
            no_text = re.findall(r'\d\d:\d\d', time) #['12:30']
            #print(no_text[0][:2]) # 12
            if tw in time:
                elem = no_text[0][:2]
                time2.append(elem)
                time2.append(no_text[0][2:])            
                result = ','.join(time2)
                result2 = result.replace(",", "")
                print(result2)
                return result2
            else:
                elem = no_text[0][:2]
                index = a_m_hour.index(elem)
                p_a_repl = p_m_hour[index]
                time2.append(p_a_repl)
                time2.append(no_text[0][2:])
                result = ','.join(time2)
                result2 = result.replace(",", "")
                print(result2)
                return result2

if __name__ == '__main__':
    assert time_converter('12:30 a.m.')
    assert time_converter('12:30 p.m.') #== '12:30'
    assert time_converter('9:00 a.m.') #== '09:00'
    assert time_converter('11:15 p.m.') #== '23:15'
    assert time_converter('11:15 a.m.')
    assert time_converter('9:00 p.m.')

"""
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
