# # 5.	HTML
# a=input()
# l=[]
# while True:
#     b=input()
#     if b=="end of comments" : break
#     l.append(b)
# print(f'<h1>\n\t{a}\n</h1>')
# print(f'<article>\n\t{l[0]}\n</article>')
# for i in range(1,len(l)):
#     print(f'<div>\n\t{l[i]}\n</div>')

# 04. Morse Code Translator
# a=[(lambda x: x.split())(x) for x in input().split(' | ')]
# d={}
# b='A	.- \
# C	-.-. \
# E	. \
# G	--. \
# I	.. \
# K	-.- \
# M	-- \
# O	--- \
# Q	--.- \
# S	... \
# U	..- \
# W	.-- \
# Y	-.-- \
# B	-... \
# D	-.. \
# F	..-. \
# H	.... \
# J	.--- \
# L	.-.. \
# N	-. \
# P	.--. \
# R	.-. \
# T	- \
# V	...- \
# X	-..- \
# Z	--..'
# b=b.replace('\n',' ').split()
# for i in range(0,len(b),2):
#     d[b[i+1]]=b[i]
# # print(a)
# for i in a:
#     t=''
#     for j in i:
#         t+=d[j]
#     print(t,end=' ')

# # 3.	Treasure Finder
# key=[(lambda x: int(x))(x) for x in input().split()]
#
# while True:
#     a=input()
#     if a=='find': break
#     b=''
#     for i in range(1,len(a)+1):
#         k=key[i%len(key)-1]
#         b+=chr(ord(a[i-1])-k)
#     t=b.split('&')[1]
#
#     c=b.split('&')[2].split('<')[1].split('>')[0]
#     print(f"Found {t} at {c}")

# # 2.	ASCII Sumator
# s1=input()
# s2=input()
# a=list(input())
# a=[(lambda x: ord(x) if ord(s1)<ord(x)<ord(s2) else 0)(x) for x in a]
# print(sum(a))

# # 1.	Extract Person Information
# n=int(input())
# for i in range(n):
#     a=input()
#     na=False
#     ag=False
#     for k in a:
#
#         if k=='@':
#             na=True
#             name=''
#             continue
#         elif k=='#':
#             ag=True
#             age=''
#             continue
#         elif k=='|':
#             na=False
#             continue
#         elif k=='*':
#             ag=False
#             continue
#         elif na: name+=k
#         elif ag: age+=k
#     print(f"{name} is {age} years old.")

# #  Winning Ticket
# a=input().split(',')
# a=[(lambda x: x.strip())(x) for x in a]
# l=['@', '#', '$' , '^' ]
#
# def check(x):
#     for i in l:
#         if 6*i in x:
#             l1=[(lambda a: a*i in x)(a) for a in range(10,5,-1)]
#             return i,10-l1.index(True)
#     return '',0
# for i in a:
#     if len(i)!=20 :
#         print("invalid ticket")
#         continue
#     x1,x2=i[:10],i[10:]
#     x1_s,x1_n=check(x1)
#     x2_s,x2_n=check(x2)
#     if x1_n==0 or x2_n==0 :
#         print(f"ticket \"{i}\" - no match")
#         continue
#     if x1_s==x2_s and x1_n==x2_n and x1_n==10:
#         print(f"ticket \"{i}\" - {x1_n}{x1_s} Jackpot!")
#         continue
#     elif x1_s==x2_s and min(x1_n,x2_n)>=6:
#         print(f"ticket \"{i}\" - {min(x1_n,x2_n)}{x1_s}")
#         continue

# Rage Quit
# a=input()
# flag=[False,False]
# word=''
# num=''
# t=''
#
# for i in range(len(a)):
#     if flag[0] and (flag[1] or i==(len(a)-1) )and (not a[i].isdigit() or i==(len(a)-1)):
#         if i==(len(a)-1): num+=a[i]
#         t=t+(word*int(num)).upper()
#         word=''
#         num=''
#         flag=[False,False]
#     if not a[i].isdigit():
#         word+=a[i]
#         flag[0]=True
#     else:
#         num+=a[i]
#         flag[1]=True
# ll=''
# for i in a.upper():
#     if not i.isdigit():ll+=i
# l1=len(set(ll))
# print(f"Unique symbols used: {l1}")
# # print(set(ll))
# print(t)

# # Letters Change Numbers
# a= input().strip()
# a=a.split()
# # a=list(filter(lambda x: x!='',a))
# t=0
# # print(a)
# for i in a:
#     first_letter=ord(i[0].lower())-96
#     last_letter=ord(i[-1].lower())-96
#     number=int(i[1:-1])
#     if i[0].isupper():
#         number= number / first_letter
#     else: number= number * first_letter
#     if i[-1].isupper():
#         number-=last_letter
#     else:number+=last_letter
#     t+=number
# print(f'{t:.2f}')

# # String Explosion
# a=input()
# i=0
# k=0
# r=''
# bomb=False
# while i < len(a):
#     if a[i]=='>':
#         bomb=True
#         r += a[i]
#         i+=1
#         continue
#     elif bomb==True:
#         k+=int(a[i])
#         bomb=False
#         k-=1
#         i+=1
#         continue
#     elif k>0:
#         k-=1
#         i+=1
#         continue
#     else:
#         r+=a[i]
#         i+=1
#         continue
# print(r)

# #   06. Replace Repeating Chars
# a=list(input())
# k=''
# for i in range(len(a)-1):
#     if a[i]!=a[i+1]:
#         k+=a[i]
# k+=a[i+1]
# print(k)

# #  Emoticon Finder
# a= input()
# l=[]
# for i in range(len(a)-1):
#     if a[i]==':' and a[i+1]!=' ':
#         l.append(a[i]+a[i+1])
# print(*l,sep='\n')

# # Caesar Cipher
# a=input()
# k=''
# for i in a:
#     k+=chr(ord(i)+3)
# print(k)

# # Extract File
# a=input().split('\\')
# a,b=a[-1].split('.')
# print(f'File name: {a} \nFile extension: {b}')

# # Character Multiplier
# a,b=input().split(' ')
# def result(a,b):
#     k=0
#     for i in range(len(a)):
#         k+=ord(a[i])*ord(b[i])
#     if len(a)==len(b): return k
#     for i in range(len(a),len(b)):
#         k+=ord(b[i])
#     return k
# if len(a)>len(b):
#     print(result(b,a))
# else: print(result(a,b))

# # 1.	Valid Usernames
# a=input().split(', ')
# l=[]
# for i in a:
#     flag=True
#     if len(i)<3 or len(i)>16: continue
#     for j in i:
#         if j.isdigit() or j.isalpha() or (j in ['-','_']): pass
#         else:
#             flag=False
#             break
#     if flag: l.append(i)
# print(*l,sep='\n')

# a=input()
# c=''
# d=''
# o=''
# for i in a:
#     if i.isdigit():d+=i
#     elif i.isalpha():c+=i
#     else : o+=i
# print(d,c,o,sep='\n')

# a= input().split(', ')
# b= input()
# for i in a:
#     while i in b:
#         b=b.replace(i,'*'*len(i))
# print(b)

# a=input()
# b=input()
# while a in b:
#   b=b.replace(a,'')
# print(b)

# a=input().split(' ')
# k=''
# for i in a:
#     k+=i*len(i)
# print(k)

# while True:
#     a=input()
#     k=''
#     if a=='end': break
#     for i in reversed(a):
#         k+=i
#     print(f"{a} = {k}")
