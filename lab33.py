def checkio(game_result):
    for i in game_result:
        if i == 'XXX':
            print('X')
            return 'X'
        if i == 'OOO':
            print('O')
            return 'O'    
    if game_result[0][0] == game_result[1][0] == game_result[2][0] == 'X':
        print('X')
        return 'X'
    if game_result[0][1] == game_result[1][1] == game_result[2][1] == 'X':
        print('X')
        return 'X'
    if game_result[0][2] == game_result[1][2] == game_result[2][2] == 'X':
        print('X')
        return 'X'
    if game_result[0][0] == game_result[1][0] == game_result[2][0] == 'O':
        print('O')
        return 'O'
    if game_result[0][1] == game_result[1][1] == game_result[2][1] == 'O':
        print('O')
        return 'O'
    if game_result[0][2] == game_result[1][2] == game_result[2][2] == 'O':
        print('O')
        return 'O'
    if game_result[0][0] == game_result[1][1] == game_result[2][2] == 'X':
        print('X')
        return 'X'
    if game_result[0][2] == game_result[1][1] == game_result[2][0] == 'X':
        print('X')
        return 'X'
    if game_result[0][0] == game_result[1][1] == game_result[2][2] == 'O':
        print('O')
        return 'O'
    if game_result[0][2] == game_result[1][1] == game_result[2][0] == 'O':
        print('O')
        return 'O'
    if game_result[0][2] == game_result[1][1] == game_result[2][0] == 'O':
        print('O')
        return 'O'
    else:
        print('D')
        return 'D'


if __name__ == '__main__':
    assert checkio(["OOO","XX.",".XX"]) == "O"
    assert checkio(["X.O","XX.","XOO"]) == "X"
    assert checkio(["OO.","XOX","XOX"]) == "O"
    assert checkio(["O.X","XX.","XOO"]) == "X"
    assert checkio(["OOX","XXO","OXX"]) == "D"    

"""
Крестики и Нолики - это игра для двух игроков (Х и О), которые расставляют эти знаки на 3х3 поле.
Игрок, который сумел разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.

Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат.
Вам дан результат игры, и вы должны решить, кто победил или что это ничья.
Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
В случае ничьи, результат должен быть "D". 


Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.

Вх. данные: Результат игры, как список (list) строк (str, unicode).
Вых. данные: "X", "O" или "D", как строка (str).

Примеры:

checkio(["X.O", "XX.", "XOO"]) == "X"
checkio(["OO.", "XOX", "XOX"]) == "O"
checkio(["OOX", "XXO", "OXX"]) == "D"

Как это используется: Эта задача поможет вам лучше понять, как работать с матрицами и вложеными массивами.
Ну и конечно, это будет полезно при разработке игр, так как надо уметь оценивать результаты.

Предусловия:
В играх может быть только один победитель или ничья.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""
