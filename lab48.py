import re
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    result = re.sub(r'  ', ' _', code)
    result2 = (re.sub(r' ', ',', result)).split(',')
    print(result) # ... --- -- . _ - . -..- -
    print(result2) # ['...', '---', '--', '.', '_', '-', '.', '-..-', '-']
    l = []
    
    for i in result2:
        print(i) # ---
        if i == "_":
            l.append(' ')
        else:
            for f,g in MORSE.items():
                if i == f:
                    print(g)
                    l.append(g)
    print(l) # ['s', 'o', 'm', 'e', ' ', 't', 'e', 'x', 't']
    print(((','.join(l)).replace(',', '')).capitalize())
    return ((','.join(l)).replace(',', '')).capitalize()

if __name__ == '__main__':
    assert morse_decoder("... --- -- .   - . -..- -") #== "Some text"
    #assert morse_decoder("..--- ----- .---- ---..") #== "2018"
    #assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") #== "It was a good day"

"""
Ваша задача - расшифровать сообщение используя азбуку Морзе.
В шифровке будет использован 1 пробел между буквами одого слова и 3 пробела между отдельными словами.
Если расшифрованный текст начинается со слова, первая буква этого слова должна быть заглавной.

Входные данные: Секретное сообщение
Выходные данные: Расшифрованный текст

Предусловия:
0 < len(message) < 100
Текст будет состоять только из цифр и букв английского алфавита.
"""

