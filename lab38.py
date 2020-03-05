import re
def checkio(expression):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    
    stack = []
    for i in expression:
        if i in brackets_open:
            stack.append(i)
            print(stack + list("1")) # ['(', '1']
            # в итоге stack = ((
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            
            index = brackets_closed.index(i) # 0, индекс закрывающей скобки берется из brackets_closed
            open_bracket = brackets_open[index] # присваиваем open_bracket = (
            if stack[-1] == open_bracket:
                stack = stack[:-1] # убираем последний элемент
            else: return False
    print(stack) # возвращает []
    print(not stack) # возвращает True
    return (not stack)

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") #== True, "Simple"
    #assert checkio("{[(3+1)+2]+}") #== True, "Different types"
    #assert checkio("(3+{1-1)}") #== False, ") is alone inside {}"
    #assert checkio("[1+1]+(2*2)-{3/3}") #== True, "Different operators"
    #assert checkio("(({[(((1)-2)+3)-3]/3}-3)") #== False, "One is redundant"
    #assert checkio("2+3") #== True, "No brackets, no problem"


"""
https://py.checkio.org/ru/mission/brackets/
Дано выражение с цифрами, скобками и операторами. В данной задаче важны только скобки.
Скобки представлены в трех вариациях: "{}" "()" и "[]". Скобки используются,
чтобы определить порядок применения операторов или ограничить участок выражения.
Если скобка открывается, то она должна закрываться скобкой того же типа.
Участки ограниченные одной парой скобок, не должны пересекаться с участками других скобок.
В этой задаче, вам необходимо определить правильное ли выражение или нет, основываясь на расположении скобок.
И не обращайте внимание на операторы и операнды.

Входные данные: Выражение для проверки, как строка (str, unicode).
Выходные данные: Решение, правильное выражение или нет, как булево значение (True или False).

Примеры:
checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
checkio("2+3") == True

Зачем это надо: Когда вы пишите большие формулы в вашем любимой математической программе.
то лишняя или пропущеная скобка может превратится в очень сильную головную боль.
И вот здесь то и необходим данный концепт, который используется во многих IDE.

Предусловия:
Выражение содержит только скобки ("{}" "()" or "[]"), цифры и/или операторы ("+" "-" "*" "/").
0 < len(expression) < 103
"""

"""
    l = []
    m = '()[]{}'
    expression_clear = re.findall(r'\D', expression)
    #print(expression_clear) #['(', '(', '+', ')', '*', '+', ')']
    for i in expression_clear:
        if i in m:
            l.append(i)
    #print(l) #['(', '(', ')', ')']
    spisok = ','.join(l)
    #print(spisok) # (,(,),)
    result = re.sub(r',', '', spisok) # (())
    print(result)
    for i in result:        
        result.replace('()', '')
    print(result)
"""
