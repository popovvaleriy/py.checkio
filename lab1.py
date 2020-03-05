import re
from collections import Counter
import string

def checkio(spisok):
    dictionary = {}
    result = sorted(re.findall(r'\w', spisok.lower()))
    print(result)
    for t in result:
        dictionary[t] = result.count(t)
        print(dictionary[t])
    print(dictionary.items())
    print(dictionary.keys())
    print(dictionary.values())
    cont = max(dictionary.values())
    print(cont)
    
    l = []
    for key in dictionary:
        if dictionary[key] == cont:
            l.append(key)
    print(l)
    
    l = sorted(l)
    print(l[0])
    return(l[0])

checkio('Lorem ipsum dolor sit amet')
