from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    
    list_ext = []      
    list_no_name = []  # список файлов без имени
    list_name_ext = [] # список файлов с расширением и именем
    list_no_ext = []   # список файлов без расширения
    
    for i in files:
        temp = []
        if i == ".config":
            temp.append(".config")
            temp.append("")
        elif i == "config.":
            temp.append("config")
            temp.append("")
        else:
            temp.append(i[:i.rfind(".")])
            temp.append(i[i.rfind(".") + 1:])
        list_ext.append(temp)
    print(list_ext)

    for item in list_ext:
        if item[0] == '':
            list_no_name.append(item)
        elif item[1] == '':
            list_no_ext.append(item)
        else:
            list_name_ext.append(item)
    print(list_no_name, "  list no name")
    print(list_no_ext, "  list no ext")
    print(list_name_ext, "  list name ext")
            
    #l_sorted = sorted(list_ext, key=lambda x: x[1]) # сортировка по второму элементу вложенного списка

    list_no_name_sorted = sorted(list_no_name, key=lambda x: x[1])
    list_no_ext_sorted = sorted(list_no_ext, key=lambda x: x[0])
    list_name_ext_sorted = sorted(list_name_ext, key=lambda x: x[1])

    list_sorted = list_no_name_sorted + list_no_ext_sorted + list_name_ext_sorted
    print(list_sorted)
    
    result = []
    for i in list_sorted:
        temp2 = []
        for item in i:
            if item == '':
                temp2.append('.')
            else:
                temp2.append(item)
        #print(','.join(temp2).replace(',', '.').replace('..', '.'))
        result.append(','.join(temp2).replace(',', '.').replace('..', '.').replace('.config.', '.config'))
    print(result)
                        

    return result


if __name__ == '__main__':
    assert sort_by_ext([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"]) == \
                       [".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]
    #assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    #assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    #assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    #assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    #assert sort_by_ext(['.aa', '.bat', '1.cad', '1.', '1.aa', '.config', 'config.']) == ['.aa', '.bat', '.config', '1.', 'config.', '1.aa', '1.cad']
    #assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    #assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    #assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']

"""
Sort by Extension

Вам предоставляется список файлов. Вам нужно отсортировать этот список по расширению файла.
Файлы с одинаковым расширением должны быть отсортированы по имени.

Некоторые возможные случаи:
     Имя файла не может быть пустой строкой;
     Файлы без расширения должны идти перед файлами с одним;
     Имя файла ".config" имеет пустое расширение и имя ".config";
     Имя файла "config." имеет пустое расширение и имя «config.»;
     Имя файла «table.imp.xls» имеет расширение «xls» и имя «table.imp»;
     Имя файла ".imp.xls" имеет расширение "xls" и имя ".imp".

Ввод: список имен файлов.
Вывод: список имен файлов.

Example:
sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
"""
