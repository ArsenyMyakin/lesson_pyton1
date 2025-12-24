# s=input()
# res=''
# for i in s:
#     code=ord(i)
#     if "A"<=i<="Z":
#         res+=chr(code+32)
#     else:
#         res+=1
# print(res)

# def statswith(str1,str2):
#     if str1<str2:
#         return False
#     else:
#         for i in range(len(str2)):
#             if str1[i]!=str2[i]:
#                 return False
#     return True

# a=input()
# sub=input()
# count=0
# for i in a:
#     if i==sub:
#         count+=1
# print(count)

def replace(st,old, new):
    if old not in st: return False
    for i in range(len(st)):
        flag=False
        for j in range(len(old)):
            if st[i+j]!=old[j]:
                flag=True
                break
