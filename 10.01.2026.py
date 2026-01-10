# b=[i for i in range(5)]
# print(b)
# [выражение for элемент in последовательность]
# b = [i for i in range(5) if i%2==0]
# print(b)
# nums=[i**2 for i in range(1,11)]
# print(nums)
# pairs={(x,y) for x in range(1,4) for y in range(1,4)}
# print(pairs)

# x=[x**2 for x in range(1,16)]
# print(x)

# a=['pyton','java','c++','javascript','go']
# x=[a.upper() for a in a]
# print(x)

# x=[0,15,20,25,30,-5,-10]
# f=[x*(9/5)+32 for x in x if x>0]
# print(f)

# q=[[1,2,3],[4,5,6],[7,8,9]]
# x=[q for q in q if q%2==0]
# print(x)

# w=['apple', 'banana', 'cherry', 'date', 'elderberry']
# dict={i:len(i) for i in w if len(i)>5}
# print(dict)

# l=['Hello world', 'программирование', 'списочные включения']
# d={i: [len(j) for j in i.split()] for i in l}
# print(d)

a={i: [j for j in range(1,i+1) if i%j==0] for i in range(1,6)}
print(a)