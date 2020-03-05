from collections import Counter
def most_frequent(data: list) -> str:
    l = []
    d = []
    for i in data:
        l.append(i)
    print(l)  # ['a', 'b', 'c', 'a', 'b', 'a']
    c = Counter(l)
    print(c)  #({'a': 3, 'b': 2, 'c': 1})
    
    val = list(c.values())
    print(val)  # [1, 2, 3]
    key = list(c.keys())
    print(key)  # ['c', 'b', 'a']
    print(key[val.index(max(val))])  # a
    return key[val.index(max(val))]

        
    #return None

if __name__ == '__main__': 
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')


"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
У вас есть последовательность строк, и вы хотите определить наиболее часто встречающуюся строку в последовательности.

Input: a list of strings.
Output: a string.

most_frequent([
    'a', 'b', 'c', 
    'a', 'b',
    'a'
]) == 'a'

most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""
