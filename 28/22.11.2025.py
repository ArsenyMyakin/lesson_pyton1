#Задача 85
# list1=input().split(" ")
# list2=input().split(" ")
# dict1={}
# dict2={}
# set1=set(list1)
# set2=set(list2)
# for i in list1:
#     dict1.update({i:list1.count(i)})
# for j in list2:
#     dict2.update({j:list2.count(j)})
# for key,value in dict1.items():
#     if key not in dict2:
#         dict2[key]=value
#     else:
#         dict2[key]+= value
# print(dict2)

#Задача 86
# str1=sorted(input().split())
# dict1={}
# for i in str1:
#     dict1.update({i:str1.count(i)})
# a=dict1.copy()
# for key,value in dict1:
#     if value > 1:
#         a.pop(key,None)
# print(a)

#Задача 88
# students = [
#     {'name': 'Alice', 'group': 'A', 'score': 85},
#     {'name': 'Bob', 'group': 'B', 'score': 92},
#     {'name': 'Charlie', 'group': 'A', 'score': 78},
#     {'name': 'David', 'group': 'C', 'score': 88},
#     {'name': 'Eve', 'group': 'B', 'score': 95}
# ]
# students2={}
# for i in students:
#     if i["group"] in students2:
#         students2[i["group"]].append(i["name"])
#     else:
#         students2[i["group"]] = [i["name"]]
# print(students2)

#Задача 87
a=input().replace(" ","")
b={}
for i in set(a):
    b[i]= a.count(i)
s=[["",0],["",0],["",0]]
for i in b:
    for j in range(len(s)):
        if s[j][1] < b[i] and [i,b[i]] not in s[j]:
        s[j][0] = i
        s[j][1] = b[i]
print(b)