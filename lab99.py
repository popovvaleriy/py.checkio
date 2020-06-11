def isometric_strings(str1: str, str2: str) -> bool:
    l = []
    for i in range(len(str1)):
        temp = []
        temp.append(str1[i])
        temp.append(str2[i])
        l.append(temp)
    print(l)

    d = {}
    for i in l:
        d[i[0]] = []
    print(d)

    for key, value in d.items():
        for i in l:
            if key == i[0]:
                value.append(i[1])       
    print(d)

    for key, value in d.items():
        print(len(set(value)))
        if len(set(value)) > 1:
            print(False)
            return False
        else:
            continue
        
    print(True)    
    return True


if __name__ == '__main__':
    #assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True

"""
Surjection Strings

А может быть это шифр? Может быть, но это не точно.

Вам надо проверить, что 2 данные строки изометричны.
Это значит что символ из одной строки может стать в соответствие символам из другой строки.

Один символ одной строки может соответствовать только одному символу другой строки. Д
ва или более символа одной строки могут соответствовать одному символу другой строки, но не наоборот.

Input: Два аргумента. Оба строки.
Output: Булеан.

Example:
isometric_strings("add", "egg") == true
isometric_strings("foo", "bar") == false
"""
