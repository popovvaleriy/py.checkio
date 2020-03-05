def checkio(time_string: str) -> str:
    dict_time = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',}
    list_time = time_string.split(':')
    print(list_time)
    for i in range(len(list_time)):
        if len(list_time[i]) == 1:
            list_time[i] = '0'+list_time[i]
    print(list_time)
   
    time_h = list_time[0]
    print(time_h)
    time_h_compl = str(dict_time.get(time_h[0]) + " " + dict_time.get(time_h[1]))
    time_h_compl_cut = time_h_compl[2:].replace('0','.').replace('1','-')
    print(time_h_compl_cut.replace('0','.').replace('1','-'))
    
    time_m = list_time[1]
    print(time_m)
    time_m_compl = str(dict_time.get(time_m[0]) + " " + dict_time.get(time_m[1]))
    time_m_compl_cut = time_m_compl[1:].replace('0','.').replace('1','-')
    print(time_m_compl_cut.replace('0','.').replace('1','-'))
    
    time_s = list_time[2]
    print(time_s)
    time_s_compl = str(dict_time.get(time_s[0]) + " " + dict_time.get(time_s[1]))
    time_s_compl_cut = time_s_compl[1:].replace('0','.').replace('1','-')
    print(time_s_compl_cut.replace('0','.').replace('1','-'))

    list_time[0] = time_h_compl_cut
    list_time[1] = time_m_compl_cut
    list_time[2] = time_s_compl_cut
    print(list_time)

    time_shablon = time_h_compl_cut+" : "+time_m_compl_cut+" : "+time_s_compl_cut

    print(time_shablon)
    
    return time_shablon

if __name__ == '__main__':
    #assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    #assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    #assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

"""
Помогите Стефану создать программный модуль для перевода времени представленного в нормальном виде,
в двоичную Морзе-форму. Взгляните на иллюстрацию, Серые кружки значат "включено", а белые - "выключено".
Каждая цифра в написании времени представлена разным количеством бинарных знаков.
Первая цифра в "часах" состоит из двух знаков, тогда как вторая цифра -- из четырех.
Первая цифра "минут" и "секунд" состоят из трех знаков и вторые цифры -- из четырех.
Каждая цифра должна быть переведена в двоичный вид.
Затем замените каждую единицу (1) на тире ("-") и каждый ноль (0) на точку (".").

Время может быть представлено в следующем виде: "hh:mm:ss", "h:m:s" или "hh:m:ss" "Пропущеные" цифры - это нули.
Для примера, "1:2:3" тоже самое, что и "01:02:03".

Окончательная морзе-форма времени должна быть написана в следующем формате:
"h h : m m : s s"

где каждая цифра - это последовательность "." и "-"

Ввод: Нормальная запись времени, представленая строкой (str).
Вывод: Переработаная морзе-форма времени, представленая строкой (str).

Предусловия:
В time_string всегда правильное время.
"""
