#Задача 5 из дз
# H=int(input())
# counter=0
# for i in range(1,H+1):
#     counter+=1
#     print(" "*(H-counter),end='')
#     for j in range(1,counter):
#         print(j,end="")
#     for j in range(counter,0,-1):
#         print(j, end="")
#     print()


# a="abcdABCD"
# for i in a:
#     print(ord(i),i)
# print("q"<"w")

# a="10A"
# print(int(str(a),16))
#
# print("\n\t")
# print('\'')
# print("\U0001F600")
# g=r"https:\\google.com\hello"
# print(g)

# string="hello world"
# print(string.find("d"))# поиск первого вхождеия подстроки
# print(string.index("d"))# возвращает индекс подстроки если такого нет - выдает ошибку
# print(string.split(" "))# делит строку по разделителю " "
# print(string.count(" "))# cчитает количество подстрок
# print(string.lower())# делает маленькии буквы
# print(string.upper())# делает большие буквы
# print(string.isdigit())# True все символы строки это числа
# print(string.isalpha()) # True если нет пробелов в строке и цифр
# print(string.isalnum())# 2 верхних метода в 1
# string="***hello world***"
# print(string.strip("*"))# удаляет выбранный символ в начале и конце строки
# print(string.replace("*","#",2))#меняет прошлый элемент на новый некоторое количество раз
# l= ["h","e","l","l","o"]
# print("-".join(l))# cоединет элементы с делителем

#Задача 2
a=input()
print(a[-4:])

#Задача 5
a=input()
print(a[0::2])



