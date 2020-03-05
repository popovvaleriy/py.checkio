def bigger_price(limit, data):
    dict_values = []
    price_list = []
    max_price = []
    lim_r = list(range(0, limit, 1)) # [0, 1]

    for i in data:
        dict_values.append(i.values())  # вытягиваем значения из словарей и добавляем в пустой список
    #print(dict_values) #[dict_values(['bread', 100]), dict_values(['wine', 138]), dict_values(['meat', 15]), dict_values(['water', 1])]
    for i,j in dict_values:       
        price_list.append(j)  #[100, 138, 15, 1]       
    price_sorted_reverse = sorted(price_list, reverse = True)  #[138, 100, 15, 1]
    for z in lim_r:
        for i in data:
            #print(i.values())
            if price_sorted_reverse[z] in i.values():  #print(i) # {'name': 'wine', 'price': 138}                
                max_price.append(i)                              
                    
    print(max_price)
    return max_price

if __name__ == '__main__':
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])
    
    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ])

"""

Дана таблица всех доступных продуктов на складе. Данные представленны в виде списка диктов (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров.
Количество товаров, которые мы ищем, будет переданно в первом аргументе, а сами данные по товарам будут переданны вторым аргументом.

Input: Число и массив диктов (int and list of dicts). Каждый дикт имеет 2 ключа "name" и "price".
Output: Такой же как и второй аргумент.

Example:

bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]


bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}]

"""
