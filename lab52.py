def checkio(number):
    FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    HUNDRED = "hundred"
    FIRST_TEN.insert(0,HUNDRED) # добавить в начало списка
    OTHER_TENS.insert(0,"")
    OTHER_TENS.insert(0,"")
    for i in SECOND_TEN:
        FIRST_TEN.append(i)
    #print(FIRST_TEN) #['hundred', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    #print(OTHER_TENS) #['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        
    if len(str(number)) == 1:
        for f in range(len(FIRST_TEN)):
            if f == number:
                result = FIRST_TEN[f]
                print(result)
        return result

    if len(str(number)) == 2:
        if int(str(number)[0:2]) >= 10 and int(str(number)[1:3]) < 20: # для чисел типа 11
            for g in range(len(FIRST_TEN)):
                if g == int(str(number)[0:2]):
                    print(FIRST_TEN[g])
                    return FIRST_TEN[g]
        if int(str(number)[0:2]) > 19:  #для чисел типа 20
            if int(str(number)[1]) == 0:
                for m in range(len(OTHER_TENS)):
                    if m == int(str(number)[0]):
                        print(OTHER_TENS[m])
                        result1 = OTHER_TENS[m]
                        return result1
            else:
                for m in range(len(OTHER_TENS)):  #для чисел типа 24
                    if m == int(str(number)[0]):
                        print(OTHER_TENS[m])
                        result1 = OTHER_TENS[m]
                for n in range(len(FIRST_TEN)):
                    if n == int(str(number)[1]):
                        print(FIRST_TEN[n])
                        result2 = FIRST_TEN[n]
                print(result1 + ' ' + result2)
                return result1 + ' ' + result2
        
    if len(str(number)) == 3:
        for i in range(len(FIRST_TEN)):
            if i == int(str(number)[0]):
                result1 = FIRST_TEN[i] + " " + HUNDRED
                print(result1)
        if int(str(number)[1:3]) == 0:
            return result1
        if int(str(number)[1:3]) != 0:
            if int(str(number)[1:3]) < 10: #print(str(number)[1:3])  # 01 # для чисел типа 103           
                for j in range(len(FIRST_TEN)):
                    if j == int(str(number)[2]):
                        print(FIRST_TEN[j])
                        result2 = FIRST_TEN[j]
                        print(result1 + ' ' + result2)
                        return result1 + ' ' + result2
            if int(str(number)[1:3]) >= 10 and int(str(number)[1:3]) < 20: # для чисел типа 111
                for g in range(len(FIRST_TEN)):
                    if g == int(str(number)[1:3]):
                        print(FIRST_TEN[g])
                        result3 = FIRST_TEN[g]
                        print(result1 + " " + result3)
                        return result1 + " " + result3
            if int(str(number)[1:3]) > 19:  #для чисел типа 124
                if int(str(number)[2]) == 0:
                    for m in range(len(OTHER_TENS)):
                        if m == int(str(number)[1]):
                            print(OTHER_TENS[m])
                            result4 = OTHER_TENS[m]
                            print(result1 + ' ' + result4)
                            return result1 + ' ' + result4
                else:
                    for m in range(len(OTHER_TENS)):
                        if m == int(str(number)[1]):
                            print(OTHER_TENS[m])
                            result4 = OTHER_TENS[m]
                    for n in range(len(FIRST_TEN)):
                        if n == int(str(number)[2]):
                            print(FIRST_TEN[n])
                            result5 = FIRST_TEN[n]
                            print(result1 + ' ' + result4 + " " + result5)
                            return result1 + ' ' + result4 + " " + result5

if __name__ == '__main__':
    #assert checkio(1)
    #assert checkio(10)
    #assert checkio(4) #== 'four', "1st example"
    #assert checkio(110)
    assert checkio(940)
    #assert checkio(88)
    #assert checkio(139)
    #assert checkio(133) #== 'one hundred thirty three', "2nd example"
    #assert checkio(14) #== 'twelve', "3rd example"
    #assert checkio(101) #== 'one hundred one', "4th example"
    #assert checkio(111)
    #assert checkio(121)
    #assert checkio(212) #== 'two hundred twelve', "5th example"
    #assert checkio(40) #== 'forty', "6th example"
    #assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

"""
Speech Module
Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел.
Для него сейчас большая проблема произносить составные числа.
Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу.
Стефан должен говорить на английском, так что вам нужно знать правила составления чисел в английском языке.
Все слова в строковом представлении числа должны быть разделены одним пробелом.
Будьте осторожны с пробелами -- очень сложно увидеть двойной пробел, но это критично для компьютера.

Вх. данные: Число, как целочисленное (int).
Вых. данные: Текстовое написание числа, как строка (str).

Примеры:
checkio(4)=='four'
checkio(143)=='one hundred forty three'
checkio(12)=='twelve'
checkio(101)=='one hundred one'
checkio(212)=='two hundred twelve'
checkio(40)=='forty'

Как это используется: Эта концепция будет полезна для программного обеспечения по синтезу речи или автоматических систем отчетности.
Также это может пригодиться при написании простого бота для чата, который будет уметь составлять числа.

Предусловия: 0 < number < 1000
"""
