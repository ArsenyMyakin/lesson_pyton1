# #ascii_lettters, ascii_uppercase, ascii_lowercase
# #diggits, punctuation
# import string
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
#
# print("hello" + "world")
# sighn = ":"
# print(f"hello{sighn}world")

#Задача 4
# import string
# from random import randint,choice
# list_pairs=[]
# for i in range(100):
#     a = choice(string.ascii_uppercase)
#     a+= f"{randint(0,9)}\n"
#     list_pairs.append(a)
# with open("test.txt","w") as file:
#     file.writelines(list_pairs)
# with open("test.txt","r") as file:
#     for i in file:
#         if int(i[1]) % 2 == 0:
# #             print(i)
# c=0
# with open("test.txt","r") as file:
#     for l in file:
#         if l[0]=="A":
#             c+=1
#     print(c)

#Задача 8
from random import randint,choice
import string
with open("test.txt","w") as file:
    for i in range(150):
        a=f"{choice(string.ascii_uppercase)}-{randint(0,9)}\n"
        print(file.write(a))
with open("test.txt","r") as file:
    for i in file:
        if int(i[2])>5:
            print(i)

