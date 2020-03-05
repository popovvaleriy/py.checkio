from typing import List, Any
List = (1, 1, 1)

def all_the_same(List):
    if len(List) == 0:
        print(True)
        return True
    for i in List:
        if List.count(i) == len(List):
            print(True)
            return True
    else:
        print(False)
        return False

all_the_same(List)

"""
from typing import List, Any

class Same:
    List = [1, 2, 1]
    
    def all_the_same(self, List):
        if len(List) == 0:
            print(True)
            return True
        for i in List:
            if List.count(i) == len(List):
                print(True)
                return True
            else:
                print(False)
                return False

Same1 = Same()

Same1.all_the_same([1, 1, 1])
Same1.all_the_same([1, 2, 1])
Same1.all_the_same(['a', 'a', 'a'])
Same1.all_the_same([])
Same1.all_the_same([1])
"""



"""

from typing import List, Any
List = (1, 1, 1)

def all_the_same(elements: List):
    if len(List) == 0:
        print(True)
        return True
    for i in List:
        if List.count(i) == len(List):
            print(True)
            return True
    else:
        print(False)
        return False

all_the_same(List)

"""

"""
def all_the_same(elements: List[Any]):
    if len(List) == 0:
        print(True)
        return True
    for i in range(len(List) - 1):
        if List[i] != List[i + 1]:   
            print(False)
            return False
        if List[0] != List[-1]:
            print(False)
            return False
        else:
            print(True)
            return True

all_the_same(List)
"""

"""В этой миссии Вам надо определить, все ли элементы массива равны.

Входные: List.

Выходные: Bool.

Примеры:

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
