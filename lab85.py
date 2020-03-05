def is_majority(items: list) -> bool:
    t_list = 0
    f_list = 0
    if items == None:
        return False
    else:
        for i in items:
            if i == True:
                t_list +=1
            else:
                f_list +=1
    print(t_list)
    print(f_list)
    if t_list > f_list:
        print(True)
        return True
    elif t_list < f_list:
        print(False)
        return False
    else:
        print(False)
        return False


if __name__ == '__main__':
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False


"""
We have an List of booleans. Let's check if the majority of elements are true.

example

Some cases worth mentioning:
1) an empty list should return false;
2) if trues and false have an equial amount, function should return false.

Input: An List of booleans.
Output: A Boolean.

Example:
is_majority([True, True, False, True, False]) == True
is_majority([True, True, False]) == True
"""
