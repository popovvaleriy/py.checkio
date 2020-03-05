def say_hi(name, age):
    a = str(name)
    b = int(age)
    print("Hi. My name is " + a + " and I'm " + str(b) + " years old")
    return "Hi. My name is " + a + " and I'm " + str(b) + " years old"

if __name__ == '__main__':
    assert say_hi("Alex", 32) #== "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) #== "Hi. My name is Frank and I'm 68 years old"
    print('Done. Time to Check.')


"""
В этой миссии вы должны написать функцию, которая представит человека по переданным параметрам.
Входные данные: Два аргумента строка(str) и положительное число(int)
Output: Строка(str).

Example:
say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
"""
