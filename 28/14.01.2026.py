# row = [[i*4+j+1 for j in range(4)] for i in range(4)]


# dicts={key:key**3 for key in range(1,11)}
# print(dicts)

# a={i**2 for i in range(1,21)}
# print(a)

# nums = [2,4,6,8,10]
# results = any(num>7 and num%3==0 for num in nums)
# print(results)

# password = "MyPass123"
# has_upper=any(i.isupper() for i in password)
# has_lower=any(j.islower() for j in password)
# has_digit=any(a.isdigit() for a in password)
# is_valid=all([has_upper,has_lower,has_digit])

# with open('901.txt') as f:
#     data = [list(map(int, i.split())) for i in f]
#
#
# def f1(line):
#     cnt_3=[i for i in line if line.count(i)==3]
#     cnt_1=[i for i in line if line.count(i)==1]
#     return len(cnt_3)==6 and len(cnt_1)==1
# def f2(line):
#     rep=[i for i in line if line.count(i) !=1]
#     norep=[i for i in line if line.count(i) ==1]
#     aver=sum(rep)/len(rep)
#     return aver<norep[0]
# for pos,val in list(enumerate(data,start=1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break


