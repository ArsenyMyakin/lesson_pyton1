#Задача 1
# def a(x):
#     z=str(x)
#     l=[]
#     for i in z:
#         l.append(i)
#     return l
# print(a())

# #Задача 2
# def words(text,**options):
#     if options.get("ignore_case"):
#         text = text.lower()
#     text_list = text.split()
#     text_set = set(text_list)
#     dict_new={}
#     for text_set_item in text_set:
#         dict_new[text_set_item] = text_list.count(text_set_item)
#     return dict_new
#
#
# print(words("hello23 World Hello",ignore_case=True,ignore_numbers=True))

#открытие файла/тип открытия/кодировка при чтении/записи
file=open("test.txt","r",encoding="utf-8")
# r - чтение
# w - запись
# a - добавлять в конец файла
# х - открывает файл для записи только если он не существует
# rb, wb, ab, xb - бинарные действия
# r+/x+ - открывает файл для чтения и записи
# w+/a+ - cм презентацию

# print(file.read())
# print(file.readline()) #счиывает одну строку
# print(file.readlines()) # считывает файл как список строк

# print(file.tell()) #позиция указаеля (число)
# file.seek(0)
#
# file.close() #закрытие файла

#контекстный менеджер
# with open("test.txt","r",encoding="utf-8") as file:
#     print(file.read())

#Задача 1
s=["hello","world","qwerty"]
with open("test.txt","w+",encoding="utf-8") as file:
    file.writelines(s)
with open("test.txt","r",encoding="utf-8") as file:
    print(file.read())