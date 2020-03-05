import re

def safe_pawns(pawns):
    pawns_index = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_index.add((row, col))
    print(pawns_index)
    print(ord('a')) #97
    print(ord('b')) #98
    print(ord('c')) #99
    print(ord('d')) #100
    print(ord('e')) #101
    print(ord('f')) #102
    print(ord('g')) #103
    count = 0
    for row, col in pawns_index:
        safe = ((row - 1, col - 1) in pawns_index) or ((row - 1, col + 1) in pawns_index)
        print(safe)
        if safe:
            count +=1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#    assert safe_pawns({"a1","a2","a3","a4","h1","h2","h3","h4"}) 
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
Входные данные: Координаты расставленных пешек в виде набора строк.
Выходные данные: Количество защищенных пешек в виде целого числа.

Пример:
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
"""

