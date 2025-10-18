#Задача 5 дз
# for i in range (1,5):
#     for j in range ((4-i),-1,-1):
#         print("*"*i+" "*j)
#         break


#Задача 15
# a=int(input())
# while True:
#     if a%2==0:
#         print("Составное")
#         break
#     if a % 3 == 0:
#         print("Составное")
#         break
#     if a % 5 == 0:
#         print("Составное")
#         break
#     if a % 7 == 0:
#         print("Составное")
#         break
#     if a % 2 != 0:
#         print("Простое")
#         break

#Задача 18
# a=int(input())
# counter=0
# x=True
# while True:
#     counter+=1
#     if a-counter==1: break
#     if (a-counter)%3==0:
#         print(a-counter)
#         x=False
#         break
# if x==True:
#     print("Таких чисел нет")


#Задача 20
# a=input()
# b="eyuioaEYUOIA"
# for i in a:
#     if i not in b:
#         print(i, end="")# end - делает в одну строку

#Задача 24



for i in range (1,8):
    if i>4:
        print("*"*(8-i))
        continue
    print("*"*i)





