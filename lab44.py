import re
def check_connection(network, first, second):
    spisok = []
    for i in list(network):  # [['dr101', 'mr99'], ['mr99', 'out00'], ['dr101', 'out00']......
        i = i.split("-")
        spisok.append(i) 
    
    l = []
    d = []
    for i in range(len(spisok)):
        if first in spisok[i]:
            l.append(spisok[i])
        else:
            d.append(spisok[i])              
    print(l) # [['scout1', 'scout2']]
    print(d) # [['dr101', 'mr99'], ['mr99', 'out00'], ['dr101', 'out00'], ['scout3', 'scout1'], ['scout1', 'scout4'], ['scout4', 'sscout'], ['sscout', 'super']]
    print('_____')

    if len(d) == 0:
        if first and second in str(l):
            print(True)
            return True
        else:
            print(False)
            return False
    if len(d) == 1:  # для d = [['mega', 'mr99']] 
        if d[0][0] in str(l) or d[0][1] in str(l):
            l.append(d[0])        
    else:
        if l[0][0] not in str(d) and l[0][1] not in str(d):
            print(False)
            return False
        else:
            counter = 0
            while counter <= len(d): # проход цикла len(d) количества раз 
                for i in range(len(d)):
                    print(d[i])
                    if d[i][0] in str(l):
                        l.append(d[i])
                        d[i] = "'',''"
                    if d[i][1] in str(l):
                        l.append(d[i])
                        d[i] = "'',''"
                    else:
                        continue
                    counter = counter + 1          
    print(d) # [['dr101', 'mr99'], ['mr99', 'out00'], ['dr101', 'out00'], "'',''", "'',''", "'',''", "'',''"]
    print(l) # [['scout1', 'scout2'], ['scout3', 'scout1'], ['scout1', 'scout4'], ['scout4', 'sscout'], ['sscout', 'super'], "'',''", "'',''", "'',''", "'',''"]
    print('_____')
    
    if second in str(l):
        print(True)
        return True
    else:
        print(False)
        return False


if __name__ == '__main__':
    assert check_connection(
        ("mr99-cat","mega-mr99",),"cat","mr99")
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
         "super", "scout2") #== True
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") #== True
    assert check_connection(
        ("night-nikola",),"nikola","night")
    assert check_connection(
        ("scout1-scout3","plane1-robin","scout3-sscout","pingin-scout1",
         "scout3-plane1","scout3-robin","plane1-nikola","plane1-pingin",
         "plane1-sobhia","scout3-sobhia","nikola-robin","sobhia-sscout",
         "robin-sobhia","robin-sscout","pingin-sscout","scout3-nikola",
         "plane1-scout1","sscout-plane1","sobhia-scout1","sscout-scout1",
         "robin-pingin","pingin-sobhia","scout3-pingin","nikola-sscout",
         "nikola-pingin","stevan-base","scout1-nikola","nikola-sobhia",
         "scout1-robin",),"base","nikola")

"""
    assert check_connection(
        ("nic-batman","cat-super",),"batman","cat")
    assert check_connection(
        ("dr101-mr99","mr99-out00","dr101-out00","scout1-scout2","scout3-scout1",
        "scout1-scout4","scout4-sscout","sscout-super"),"dr101", "sscout") #== False    

"""    

"""
Подручные дроны Софии - это не какие-то тупые, бесчувственные железяки. Более того - они умеют дружить.
На самом деле, они уже даже делают свою социальную сеть, только для дронов!
София вытащила оттуда данные о всех связях между дронами и теперь хочет изучить эти взаимосвязи подробнее.

Дан массив прямых связей между дронами - кто с кем дружит.
Каждая такая связь представлена, как строка с двумя именами разделеными дефисом.
Для примера: "dr101-mr99" означает что dr101 и mr99 дружат между собой.
Кроме этого даны два имени. Попробуйте определить, связаны ли они через других дронов, вне зависимости от глубины этих связей.
Для примера: Если у двух дронов есть общий друг или друзья, у которых есть общий друг и так далее.

network

Давайте рассмотрим примеры:
scout2 и scout3 оба дружат с scout1, так что они связаны. super и scout2 связаны между собой через sscout, scout4 и scout1.
Но вот dr101 и sscout никак не взаимосвязаны друг с другом.

Ввод: Три аргумента: информация о друзьях, как кортеж (tuple) строк (str); первое имя, как строка (str); второе имя, как строка (str).
Вывод: Связаны ли указанные дроны между собой, как булево значение (bool).

Примеры:
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"), "scout2", "scout3") == True

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2", "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"dr101", "sscout") == False

Связь с реальной жизнью: Данная идея может помочь вам в нахождении сложных взаимосвязей между событиями,
которые на первый взгляд не имеют никакой связи. Ну и конечно узнаете немного о социальных сетях.

Предусловие: len(network) ≤ 45
если "name1-name2" в network, то "name2-name1" не в network
3 ≤ len(drone_name) ≤ 6
first_name и second_name всегда в network.
"""
"""
    else:
        #should_restart = True
        counter = 0
        while counter <= len(d): # проход цикла len(d) количества раз 
            for i in range(len(d)):
                if (d[i][0] in str(l)) or (d[i][1] in str(l)) or (d[i][0],d[i][1] in str(l)):
                    l.append(d[i])
                    d[i] = "'',''"               
                counter = counter + 1
                #should_restart = True          
        print(d) # [['dr101', 'mr99'], ['mr99', 'out00'], ['dr101', 'out00'], "'',''", "'',''", "'',''", "'',''"]
        print(l) # [['scout1', 'scout2'], ['scout3', 'scout1'], ['scout1', 'scout4'], ['scout4', 'sscout'], ['sscout', 'super'], "'',''", "'',''", "'',''", "'',''"]
        print('_____')
"""
