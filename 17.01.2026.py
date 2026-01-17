# dict_students=[
#     {"name": "Jonn", "age":"25", "grade":"10"},
#     {"name": "Борис", "age":"18", "grade":"1"},
#     { "name": "Аркадий", "age":"30", "grade":"4"}
# ]
# get_name=lambda student: student.get("name")
# get_age=lambda student: student.get("age")
# get_student=lambda student: student.get("grade") if student.get("grade") > 3 else None
#
# names = [get_name(student) for student in dict_students]
# ages = [get_age(student) for student in dict_students]
# grades = [get_student(student) for student in dict_students if get_student(student)]
#
# print(names)
# print(ages)
# print(grades)

# unsorted_list=[4,3,2,5,1]
# print(sorted(unsorted_list))

# words=["Arseny", "my", "name"]
# sorted_words=sorted(words, key=len)
# print(sorted_words)

# dict_students=[
#     {"name":"John","age":25,"score":98},
#     {"name":"Борис","age":10,"score":77},
#     {"name":"Аркадий","age":30,"score":92},
#     {"name":"hellokitty","age":30,"score":84},
#     {"name":"АркадийПаравозов","age":30,"score":85}
# ]
# a = sorted(dict_students,reverse=True,key=lambda student:student["score"])
# print(a)

# a=lambda x: len(x)*8
# print(a("hello"))

def my_logger(func,num):
    print(f"Передано число:{num}.\n"
          f"Результат:{func(num)}"
          )
my_logger(lambda x: x**3, 5)

