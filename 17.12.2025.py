#Задача 1
# x = input().split(" ")
# a = int(x[0])
# b = int(x[1])
# c = int(x[2])
# print("Значение переменной а:", a)
# print("Значение переменной b:", b)
# print("Значение переменной c:", c)

#Задача 2
# x = input().split()
# print(int(x[0])+int(x[2])," ", int(x[1])*int(x[3]))

#Задача 3
# a = input()
# b = 1
# for i in a:
#     b*=int(i)
# print(a,": ",b,sep='')

#Задача 4
# a = input().split()
# print("Первое число: ", int(a[0]) + int(a[1])*3)
# print("Второе число: ", int(a[1]) - int(a[0])%2)

#Задача 5
# a = int(input())
# if a % 2 == 0:
#     print("Число без изменений:", a)
# else:
#     print("Удвоенное число:", a*2)

#Задача 6
# a = input()
# s = []
# for i in a:
#     s.append(i)
# if int(s[2])%2!=0 or int(s[0])%2==0:
#     print(int(a)+1)
# elif s[2]==3 or s[2]==7 or s[2]==9:
#     print(int(a)-1)
# else:
#     print(int(a))

#Задача 7
# x = int(input())
# if x > 0:
#     print(3*x+1)
# if x == 0:
#     print(x)
# if x < 0:
#     print(x**2 + 2)

#Задача 8

#Задача 9
# a = input()
# x=0
# for i in a:
#     x+=int(i)
# print("Введенное число:",a)
# print("Сумма всех разрядов:",x)

#Задача 10
# a=input().split(",")
# print(str(a).find(a[1]))

#Задача 11
# a=input().split()
# x=[]
# for i in a:
#     x.append(i[::-1])

#Задача 12
a=input().split(",")
count=0
for i in a:
    count+=1
    print("Строка ",count,": ",i, sep="")



























