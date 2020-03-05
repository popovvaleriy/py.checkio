#шаги:
#1. Настройте граф городов
#2. Разместите одну электростанцию заданного диапазона в одном городе.
#   а. Выполните поиск в ширину, чтобы определить, какие дополнительные города включены. Сохраните результат в наборе.
#   б. Повторите, положив такую же электростанцию в другой город.
#   с. Повторите весь процесс для электростанции с другим диапазоном.

#3. Рассмотрите все меры и перестановки электростанций в городах.
#   а. Возьмите объединение ранее созданных наборов, чтобы найти, какие города работают.

#   Преимущество: все BFS должны выполняться только один раз.
#   Недостаток: все BFS должны выполняться как минимум один раз.

from typing import Set, Tuple, List, Dict
from itertools import permutations
from collections import deque, defaultdict

def power_plants(connections: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    # Настройте городскую сеть
    network = defaultdict(list)
    for city0, city1 in connections:
        network[city0].append(city1)
        network[city1].append(city0)

        # Альтернативный подход?
        # for city_a, city_b in ((city0, city1), (city1, city0)):
        #    network[city_a].append(city_b)

    num_cities = len(network)
    num_plants = len(ranges)

    # Определите города с питанием, когда в каждом городе находится одна электростанция каждого диапазона.
    results = {}
    for rng in ranges:
        if rng not in results:
            sub_results = {}
            for start_city in network.keys():
                powered = set()
                visited = set()
                queue = deque([(start_city, 0)])
                while queue:
                    city, dist = queue.pop()
                    powered.add(city)
                    new_dist = dist + 1
                    if new_dist <= rng:
                        for next_city in network[city]:
                            if next_city not in visited:
                                visited.add(next_city)
                                queue.appendleft((next_city, new_dist))
                sub_results[start_city] = powered.copy()
            results[rng] = sub_results.copy()

    # Рассмотрим каждую перестановку мест расположения электростанций

    for plants in permutations(network.keys(), num_plants):
        powered_cities = set.union(*(results[ranges[i]][city]
                                     for i, city in enumerate(plants)))
        if len(powered_cities) == num_cities:
            return {city: ranges[i] for i, city in enumerate(plants)}
    print({city: ranges[i] for i, city in enumerate(plants)})
    return {}

if __name__ == '__main__':
    #assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    #assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    #assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

"""
Эта миссия является еще одной версией миссии «Электропитание».
Вы должны правильно разместить данные электростанции и снабжать энергией все города.

Междугородная сеть и радиус действия каждой электростанции приведены в качестве входных значений.
Электростанция может обеспечить электроэнергией город, в котором она находится, и в пределах ее досягаемости.
Вы должны вернуть словарь, где ключ - город, в котором вы разместите электростанцию, а значение - его диапазон.

NOTE:

Вам всегда будет дано достаточно или больше силовых установок.
Поэтому не всегда необходимо возвращать все места размещения электростанций.

Example:
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

Input:
    Междугородная сеть представлена в виде набора соединений, где каждое соединение представляет собой кортеж из двух узлов, соединенных друг с другом.
    Ассортимент каждой силовой установки представлен в виде списка целых чисел.

Output:
    Словарь мест размещения, где каждый ключ - это город, в котором вы разместите электростанцию,
    а каждое значение - соответствующий диапазон.

Precondition:
    3 ≤ number of cities ≤ 50
    1 ≤ number of power-plants
    range of power-plant ≥ 0
"""
