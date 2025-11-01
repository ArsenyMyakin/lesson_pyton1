# #Задача 2 из дз
# a=input()
# print("есть число" if a.alpha() else "числа нет")

#Задача 27
# a=input()
# print(a.islower())
# print(a.isupper())
# print(a.istitle())

#Задача 30
# a=input()
# s="1234567890"
# z=""
# x1=" "
# x2=""
# for i in a:
#     for j in s:
#         if i==j:
#             z+=i
# if z.isdigit():
#     print(a.upper())
# for i in a:
#     for j in x1:
#         if i==j:
#             x2+=i
# if not(x2.isalnum()):
#     print(a.replace(" ","*"))

#Задача 32
# a=input()
# s="eyuioaEYUIOAуеыаоэяиюУЕЫАОЭЯИЮ"
# z=0
# alpha=""
# for i in s:
#     q=a.rfind(i)
#     if z<q:
#         z=q
#         alpha=i
# print(z,alpha)

#Задача 31
# s="abcd defg ghij"
# s=s.replace(" ","")
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,"")
# print(s)

#Задача 20
# import random
# a=input()
# while True:
#     s=random.choice(a)
#     a=a.replace(s,"")
#     print("Удаляеем букву",s,":",a)
#     if a=="":
#         break

#Задача 19
a=input()
k="АВЕКМНОРСТУХ"
if len(a)==6:
    num=a[1:4]
    alp=a[0]+a[4:]
    print(num.isdigit() and alp[0] in k and alp[1] in k and alp[2] in k)
else:
    print(False)


