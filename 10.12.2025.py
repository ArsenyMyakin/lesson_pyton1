# with open("902.txt","r") as f:
#     count = 0
#     for line in f:
#         s=line.split()
#         d=[]
#         for i in s:
#             d.append(int(i))
#         d=sorted(d)
#         if d[-1] > sum(d[:-1]):
#             count+=1
#         flag = True
#         count_a=0
#         for i in range(len(d)):
#             count_c=-1
#             for j in range(len(d)):
#                 if d[i]==d[j]:
#                     count_c+=1
#             if count_c > 1:
#                 count_a+=1
#             if count_a != 1:
#                 flag = False
#                 break
#
#         if d[-1] > sum(d[:-1]) and count_a == 1:
#             count+=1
#     print(count)

# with open ("900.txt","r") as f:
#     count=0
#     for line in f:
#         numbers = line.split("\t")
#         s=[]
#         for i in numbers:
#             s.append(int(i))
#         first=[]
#         second=[]
#         for x in set(s):
#             if s.count(x) == 3:
#                 count+=1
#             if count == 1:
#                 amount_lines += 1
#
#         for i in s:
#

with open("905.txt","r") as f:
    amount_lines = 0
    for line in f:
        numbers = line.split()
        s = []
        for i in numbers:
            s.append(int(i))

        if len(set(s)) == 3 and s.count(max(s)) > 1:
            amount_lines += 1
    print(amount_lines)



