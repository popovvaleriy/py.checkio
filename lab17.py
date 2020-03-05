def checkio(number: int) -> str:
    FiBu = 'Fizz Buzz'
    Fi = 'Fizz'
    Bu = 'Buzz'
    if number <= 1000:
        if number%3 == 0 and number%5 == 0:            
            print('Fizz Buzz')
            return str(FiBu)
        if number%3 == 0:
            print('Fizz')
            return str(Fi)
        if number%5 == 0:
            print('Buzz')
            return str(Bu)
        else:
            print(number)
            return str(number)
        

    #return str(number)


if __name__ == '__main__':
    assert checkio(15)# == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6)# == "Fizz", "6 is divisible by 3"
    assert checkio(5)# == "Buzz", "5 is divisible by 5"
    assert checkio(7)# == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.

Входные данные: Число, как целочисленное (int).
Выходные данные: Ответ, как строка (str).

Примеры:
checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"

Как это используется: Здесь вы можете научиться как писать простейшую функцию и работать с if-else.
Предусловия: 0 < number ≤ 1000


______________________
# You can import some modules or create additional functions

def checkio(number: int) -> str:

    return str(number)

# Some hints:
# Convert a number in the string with str(n)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""
