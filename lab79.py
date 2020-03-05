MONSTERS = [
    'skeleton',
    'ghost',
    'jack',
    'vampire',
    'witch',
    'mummy',
    'zombie',
    'werewolf',
    'frankenstein',
]


def subtract_monster(spell: str, monster: str) -> str:
    lst = list(spell)
    for c in monster:
        lst.remove(c)
    return ''.join(lst)

def count_monsters(spell: str, i: int) -> int:
    max_cnt = 0

    for j, m in enumerate(MONSTERS[i:]):
        try:
            remain = subtract_monster(spell, m)
            cnt = 1 + count_monsters(remain, j)
            if cnt > max_cnt:
                max_cnt = cnt
        except ValueError:
            pass
    return max_cnt


def halloween_monsters(spell: str)-> int:

    return count_monsters(spell, 0)




if __name__ == '__main__':
    #assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    #assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    #assert halloween_monsters('nafrweiicttwneshhtikcn') #== 3
    #assert halloween_monsters('casjokthg') #== 2
    #assert halloween_monsters('uksnhpqptcuzwmvxcymbzqaaithnqknosgydifflvrelybhoubnfjlvvdpddkemctswfhzugomarrixwxjjigpszrc') #== 8
    #assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    #assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'

"""
Вы должны вызывать монстров из другого мира в рамках подготовки к Хэллоуину.

Вам дают строку в качестве входного значения. Вы должны использовать его,
чтобы сделать имена монстров и вернуть максимальное количество.
Вы можете назвать только 9 видов монстров:
    frankenstein
    ghost
    jack
    mummy
    skeleton
    vampire
    werewolf
    witch
    zombie

NOTE:
Вы можете сделать несколько имен монстров одного вида.
Вам не нужно использовать все символы.
Если вы не можете сделать имя монстра, верните 0.

Вход: заклинание (строка).
Вывод: количество монстров (целое число).

Precondition:
all(re.fullmatch('[a-z]', i) for i in input)
len(input) ≤ 100

Как это используется: Для расчета материалов и изделий. 
"""
