import re
def from_camel_case(name):
    l = []
    for i in name:
        if i.istitle() and i != name[0]:
            l.append('_'+i)
        else:
            l.append(i)
    print(l) #['M', 'y', '_F', 'u', 'n', 'c', 't', 'i', 'o', 'n', '_N', 'a', 'm', 'e']
    print((((','.join(l)).replace(',', ''))).lower()) # my_function_name
    return (((','.join(l)).replace(',', ''))).lower()

if __name__ == '__main__':
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"

"""
Conversion from CamelCase
Ваша задача - написать функцию, которая преобразовывает текст (название другой функции)
из формата CamelCase, принятого в JavaScript (MyFunctionName) в формат, принятый в Python (my_function_name),
где все буквы - маленькие, а слова соединены знаком нижнего подчеркивания "_".

Входные данные: Название функции как строка в CamelCase
Output: То же самое название, но в under_score

Примеры:
from_camel_case("MyFunctionName") == "my_function_name"
from_camel_case("IPhone") == "i_phone"
from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
from_camel_case("Name") == "name"

Как это используется: Чтобы применять названия функций в том стиле,
в каком они приняты в определенном языке (Python, JavaScript, и т.д.).

Предусловия:
0 < len(string) <= 100
Во входящих данных не будет чисел или пустых строк
"""
