def navigation(seaside):
    first_point_index = [0, 0]
    M_index = [0 ,0]
    C_index = [0 ,0]
    S_index = [0 ,0]
    
    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'Y':
                first_point_index = [i, j]
            elif seaside[i][j] == 'C':
                C_index = [i, j]
            elif seaside[i][j] == 'M':
                M_index = [i, j]
            elif seaside[i][j] == 'S':
                S_index = [i, j]

    print(first_point_index, "Y")
    print(M_index, 'M')
    print(C_index, 'C')
    print(S_index, 'S')
    m_route = max(abs(first_point_index[0] - M_index[0]), abs(first_point_index[1] - M_index[1]))
    c_route = max(abs(first_point_index[0] - C_index[0]), abs(first_point_index[1] - C_index[1]))
    s_route = max(abs(first_point_index[0] - S_index[0]), abs(first_point_index[1] - S_index[1]))
    print(max(abs(first_point_index[0] - M_index[0]), abs(first_point_index[1] - M_index[1])), 'm_route')
    print(max(abs(first_point_index[0] - C_index[0]), abs(first_point_index[1] - C_index[1])), 'c_route')
    print(max(abs(first_point_index[0] - S_index[0]), abs(first_point_index[1] - S_index[1])), 's_route')

    print(m_route + c_route + s_route, 'summ_route')
    
    return m_route + c_route + s_route

if __name__ == '__main__':
    #assert navigation([['Y', 0, 0, 0, 'C'],[ 0, 0, 0, 0, 0],[ 0, 0, 0, 0, 0],['M', 0, 0, 0, 'S']]) == 11

    #assert navigation([[ 0,  0, 'C'],
    #                   [ 0, 'S', 0],
    #                   ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9

"""
Compass, Map and Spyglass
Казалось бы - короткое путешествие, которое должно было занять менее одного дня - что могло пойти не так?
И тем не менее, когда остров уже был виден на горизонте, внезапно начался ужасный шторм!
Сложно передать словами, что пришлось пережить вам и вашим людям. Точнее…
В живых до острова добрались только вы - оба корабля были разрушены огромными волнами еще в море,
а остатки их корпусов были окончательно раздроблены прибрежными скалами.
Возможно, еще кому-то из вашей команды удалось выжить, но это было весьма маловероятно.
Теперь перед вами стояло 2 задачи - забрать из замка Гиперкуб и найти способ уплыть с этого проклятого острова.

Давайте решать проблемы по-порядку. Для начала вам необходимо найти компас, карту и подзорную трубу,
чтобы сориентироваться на местности.
Поторопитесь, так как природа весьма непредсказуема и если вы не успеете забрать вещи - их поглотит прибрежный песок или волнами смоет в море.

Ваша задача - посчитать суммарное количество шагов которое потребуется,
чтобы подобрать все 3 предмета - ('C' - compass), ('M' - map), ('S' - spyglass), считая от вашей стартовой позиции.
Таким образом, итоговый результат будет суммой трех дистанций: от Y к C, от Y к M и от Y к S (не Y-C-M-S).
Учтите, что вы можете ходить в 8 направлениях - влево, вправо, вверх, вниз и по диагонали в любую сторону. Ваша стартовая позиция - 'Y'.

Входные данные: Массив с расположением предметов.
Выходные данные: Длина маршрута.

Пример:

navigation([['Y', 0, 0, 0, 'C'],
            [ 0,  0, 0, 0,  0],
            [ 0,  0, 0, 0,  0],
            ['M', 0, 0, 0, 'S']]) == 11 #4 шага от Y к C, 4 от Y к S и 3 от Y к M

Как это используется: Для поиска длины пути.

Предусловия:
3x3 <= размер массива <= 10x10
"""