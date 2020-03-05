import re
data = 'ULFFunH8ni'
def checkio(data: str):
    if len(data)> 9:
        if re.search(r"[0-9]+", data) and re.search(r"[a-z]+", data) and re.search(r"[A-Z]+", data):
            return True                                                                        
        else:
            return False            
    else:
        return False

checkio('ULFFunH8ni')

    


 Стефан и София забывают о безопасности и используют простые пароли для всего. Помогите Николе разработать модуль для проверки паролей на безопасность. Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.

Вх. данные: Пароль как строка.

Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть сконвертирован и представлен как булево значение (True или False)

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True


Предусловия:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64 
"""





