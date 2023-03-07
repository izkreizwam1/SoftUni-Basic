# Letters Change Numbers
a= input().split(' ')
t=0
for i in a:
    f=ord(i[0].lower())-96
    s=ord(i[-1].lower())-96
    k=int(i[1:-2])
    if i[0].isupper():
        k=k/f
    else: k=k*f
    if i[-1].isupper():
        k-=s
    else:k+=s
    t+=k
print(f'{t:.2f}')

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
