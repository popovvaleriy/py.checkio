def flatten(dictionary):
    #print(dictionary.values(), "   values")

    if all(isinstance(val, str) for val in dictionary.values()):
        return dictionary

    D = {}
    for key, val in dictionary.items():
        print(dictionary, '  dict_test')
        if isinstance(val, str):
            D[key] = val
            print('  test1')
        elif not val:
            D[key] = ''
            print('  test2')
        else:
            print(val, "  val_2")
            print(flatten(val), "  flatten(val)") # подставляются в функцию значение ключа вместо начального словаря
            for k, v in flatten(val).items():
                D[key + '/' + k] = v
    print(D)
    return D


if __name__ == '__main__':
    #assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) #== {"key/deeper/more/enough": "value"}
    #assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    #assert flatten({"name": {"first": "One", "last": "Drone"}, "job": "scout", "recent": {}, "additional": {"place": {"zone": "1", "cell": "2"}}})
    #assert flatten({"name": {
    #                   "first": "One",
    #                    "last": "Drone"},
    #                "job": "scout",
    #                "recent": {},
    #                "additional": {
    #                    "place": {
    #                        "zone": "1",
    #                        "cell": "2"}}}
    #) == {"name/first": "One",
    #      "name/last": "Drone",
    #      "job": "scout",
    #      "recent": "",
    #      "additional/place/zone": "1",
    #      "additional/place/cell": "2"}

"""
Никола обожает классифицировать все, что видит вокруг.
Однажды Стефан подарил ему устройство для ярлыков на день рождение,
и затем они неделями отдирали наклейки со всех поверхностей и вещей на корабле.
Он категоризировал все реагенты в своей лаборатории, книги в библиотеке и даже заметки на столе.
Но когда он узнал о том, что в Python есть тип данных словарь, он категоризировал все конфигурационные файлы дронов Софии.
Теперь эти файлы организованы в сложную вложенную структуру, что очень не нравится Софии.
Помогите ей упростить эти словари словарей.

Словари - это удобный тип данных для хранения и обработки различных конфигураций.
Они позволяют хранить данные по ключам и создавать вложенные структуры.
Дан словарь, в котором в качестве ключей используются строки, а в качестве значений строки или словари.
Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах.
Результатом будет словарь без вложенных словарей.
Ключи должны содержать путь, составленный из родительских ключей из начального словаря, разделенных "/".
Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой (""). Взглянем на пример:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

Результатом будет:

{"name/first": "One",           #один прародитель
 "name/last": "Drone",
 "job": "scout",                #ключ корневого уровня
 "recent": "",                  #пустой словарь
 "additional/place/zone": "1",  #третий уровень
 "additional/place/cell": "2"}

Входные данные: Оригинальный словарь (dict).
Выходные данные: "Плоский" словарь (dict).

Предусловия:
Ключи в словаре - не пустые строки.
Значения в словаре - строки или другие словари.
root_dictionary != {}
"""
