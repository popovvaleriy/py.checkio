import re
text = "state secret"
step = -13

#print(ord('a')) print(chr('97'))

def to_encrypt(text, step):
    alf = "abcdefghijklmnopqrstuvwxyz"
#    print(alf)   
    l = []
    z = step

    if step < 0:
        alf = alf*(len(text)-step)
        for i in text:
            if i == " ":
                l.append(" ")
            else:
                aa = text.find(i)
                bb = alf.find(i)
                if text[aa] == alf[bb]:
                    l.append(alf[bb + z])
    if step > 0:
        alf = alf*(len(text)+step)
        for i in text:
            if i == " ":
                l.append(" ")
            else:
                aa = text.find(i)
                bb = alf.find(i)
                if text[aa] == alf[bb]:
                    l.append(alf[bb + z])

  
    result = ','.join(l) # преобразовать список в строку ['z', 'u', 'p', ' ', 'k', 'f', 'a', 'v'] --> z,u,p, ,k,f,a,v
    result2 = re.sub(r',', '', result) # убираем запятые в строке и получаем zup kfav
    print(result2)
    return result2

to_encrypt("state secret", -13)



"""

Ваша миссия - зашифровать текст сообщения (в исходных данных не будет
специальных символов вроде "!", "&", "?", только текст и пробелы)
используя шифр Цезаря где каждая буква исходного текста заменяется другой,
которая находится на определенном расстоянии в алфавите. Например, ("a b c", 3) == "d e f"


Входные данные: Секретное сообщение как строка (только маленькие буквы и пробелы)

Output: Тот же самый текст, но зашифрованный

Примеры:

to_encrypt("a b c", 3) == "d e f"

to_encrypt("a b c", -3) == "x y z"

to_encrypt("simple text", 16) == "iycfbu junj"

to_encrypt("important text", 10) == "swzybdkxd dohd"

to_encrypt("state secret", -13) == "fgngr frperg"

"""
