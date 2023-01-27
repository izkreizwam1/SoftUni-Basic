# l=[int(input()),int(input())]
# print(f'Before:\na = {l[0]}\nb = {l[1]}\nAfter:\na = {l[1]}\nb = {l[0]}')

# Prime Number Checker

# a=int(input())
# for i in range(2,a):
#     if a%i==0:
#         print('False')
#         exit()
# print('True')

# Decrypting Messages

# a=int(input())
# b=int(input())
# l=[]
# for i in range(b):
#     l.append(ord(input()))
#
# print(''.join([chr(x +a) for x in l]))

#  Balanced Brackets

a=int(input())
o=c=f=m=0

for i in range(a):
    k=input()
    if k=='(':
        o+=1
        f+=1
        m=0
    if k==')':
        c+=1
        f=0
        m+=1
    if f>1 or m>1 or c>o:
        print('UNBALANCED')
        exit()
if o==c: print('BALANCED')
else: print('UNBALANCED')

