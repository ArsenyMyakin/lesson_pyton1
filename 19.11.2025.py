# sets={"key":"value"} # словарь с элементом {ключ: значение} (dict)
# print(sets["key"])
# my_dict = [
#     ("ключ1","значение1")
#     ("ключ1","значение1")
#     ("ключ1","значение1")
# ]
# print(my_dict, dict(my_dict))
#d={} #dict
#d={1,2} #set
#b={str([1,2,3]):3,3:5}
#print(b[str([1,2,3])])

# d={"key1":"value1"}
# #print("key2" not in d) # есть ли ключ в словаре d?
# d["key1"] = 100
# d["key2"] = 1000
# del d["key1"]
# print(d)
# d = {"key1":"value1","key2":"value2"}
# for i in d:
#     print(i,d[i])

# print(list(d.items())) # получает все элементы словаря как список кортежей
# for i,j in d.items():
#     print(i,j)

# print(list(d.items())) # возвращет список значений
# print(list(d.keys())) #список ключей

# print(d.get("key1", 10)) # get(ключ, значение если нет такго ключа)
# print(d.pop("key3",10),d) #удаляет элемент и возвращает значение

# print(d.popitem()) # удаляет и возвращает плследний элемент

# d.update({"key3":"value3"}) # добавляет элемент
# print(d)

#d.clear()

# d = {"key1":"value1","key2":"value2"}
#
# a=d.copy() #создает копию
# a["key3"]="value100"
# print(d, a)

# keys = ["key1", "key2", "key3", "key4"]
# new_dict = dict.fromkeys(keys,10)
# print(new_dict)

#Задача 69
# dict={}
# dict["name"]="Алиса"
# print(dict)

#Задача 71
# points={"x":10}
# print(points.get("y",0))

#Задача 74
# books = {"романы":10,"детективы":5}
# books.update({"фантастика":"8"})
# print(books)

#Задача 79
# marks = {"Информатика":5,
#          "Математика":5,
#          "Русский":3,
#          "История":4,
#          "Физика":4}
# print(sum(marks.values())/len(marks))

#Задача 80
# a=input().split(" ")
# s={}
# k=[]
# for  i in a:
#     key, value=i.split(":")
#     s[key] = int(value)
# print(s,"\n",dict(k))

#Задача 81
students = ["Анна",5,"Борис",4,"Вера",5]
f={}
for i in range(0,len(students),2):
    f[students[i]]=students[i+1]
print(f)