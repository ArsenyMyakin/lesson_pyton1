from itertools import count
from operator import index

#math - библиотека для мат вычеслений
#random - библиотека для генерации псевдослучайных чисел

# import math #вызываем библиотеку (как коробку)
# from math import sqrt #вызываем инструмент from math
# import math as mth #меняем название модуля и вызываем

# import math
# print(math.sqrt(25))

# from math import * #- все инструменты из библиотеки
# from math import pow
# print(pow(10,10))

# import math as mth
# print(mth.pow(10,10))


# from random import randint,choice
#
# # index=randint(0,4) #от какого до какого числа сделать
# l=["a","b","c","d","e"]
# print(choice(l))

#Задача 9
# a=input()
# index = len(a)//2
# j=a[:index]
# b=a[index:]
# print(b+j)

#Задача 14
# a=input()
# x=a[0::2]
# z=a[1::2][::-1]
# print(x+z)

#Задача 15
# a=input()
# counter=0
# for i in range(0,len(a)-2):
#     print(a[i:i+3])

#Задача 12
# a="шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс"
# a=a.replace(", ","")
# for i in a.split():
#     print(i)
#     x=a[::-1]
#     if a == x:
#         print(x)

#Задача 16
# a=input()
# alpha=""
# amount=0
# # set - уникализирует список
# for i in set(a):
#     count=a.count(i)
#     if a.count(i)>amount:
#         alpha=i
#         amount=count
# print(alpha,"-", amount)
# print(a[::3])
# indexes=""
# maxim = 0
# for i in set(a):
#     if a.count(i)==1:
#         continue
#     bacward=a.rfind(i)
#     forward=a.find(i)
#     if (bacward-forward) > maxim:
#         maxim=bacward-forward
#         indexes=a[bacward:forward]
# print(indexes)



