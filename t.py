# # Messages Manager
# n= int(input())
# d={}
#
# while True:
#     b= input()
#     if b=='Statistics': break
#     b=b.split('=')
#     if b[0]=='Add':
#         if b[1] in d: continue
#         d[b[1]]=[int(b[2]),int(b[3])]
#
#     elif b[0]=='Message':
#         if b[1] in d and b[2] in d:
#             d[b[1]][0]+=1
#             if sum(d[b[1]])>=n :
#                 del d[b[1]]
#                 print(f"{b[1]} reached the capacity!")
#             d[b[2]][1]+=1
#             if sum(d[b[2]])>=n :
#                 del d[b[2]]
#                 print(f"{b[2]} reached the capacity!")
#
#     elif b[0]=='Empty':
#         if b[1]=='All': d={}
#         elif b[1] in d : del d[b[1]]
#
# print(f"Users count: {len(d)}")
# for i in d:
#     print(f'{i} - {sum(d[i])}')
#
# #  Message Translator
# import re
# n=int(input())
# r=r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
# for i in range(n):
#     a=input()
#     t=re.findall(r,a)
#     if bool(t):
#         print(t[0][0],end=': ')
#         for j in t[0][1]:
#             print(f'{ord(j)}', end=' ')
#         print('')
#     else:
#         print("The message is invalid")
#
# # Decrypting Commands
# a= input()
#
# while True:
#     b= input()
#     if b=='Finish': break
#     b=[int(x) if x.isdigit() else x for x in b.split()]
#     # print(b)
#     if b[0]=='Replace' :
#         a=a.replace(b[1],b[2])
#         print(a)
#     elif b[0]=='Cut' :
#         if 0<=int(b[1])<len(a) and 0<=int(b[2])<len(a):
#             a=a[:b[1]]+a[b[2]+1:]
#             print(a)
#         else:
#             print('Invalid indices!')
#     elif b[0]=='Make' :
#         if b[1]=='Upper':
#             a=a.upper()
#         elif b[1]=='Lower':
#             a=a.lower()
#         print(a)
#     elif b[0]=='Check' :
#         if b[1] in a:
#             print(f"Message contains {b[1]}")
#         else: print(f"Message doesn't contain {b[1]}")
#     elif b[0]=='Sum' :
#         if 0<=int(b[1])<len(a) and 0<=int(b[2])<len(a):
#             sum=0
#             for i in a[b[1]:b[2]+1]:
#                 sum+=ord(i)
#
#         else:
#             print('Invalid indices!')
#             continue
#
#         print(sum)
