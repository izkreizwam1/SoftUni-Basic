# l=[input(),input(),input()]
# l.reverse()
# print(l)

# n=int(input())
# l=[]
# for i in range(n): l.append(input())
# print(l)

# n=int(input())
# ln=[]
# lp=[]
# for i in range(n):
#     a=int(input())
#     if a<0: ln.append(a)
#     else: lp.append(a)
# print(f'{lp}\n{ln}\nCount of positives: {len(lp)}\nSum of negatives: {sum(ln)}')

# n=int(input())
# w=input()
# l=[]
# k=[]
# for i in range(n):
#     l.append(input())
#     if w in l[-1]: k.append(l[-1])
# print(l,k, sep='\n')

n=int(input())
l=[]
k=[]
for i in range(n):
    l.append(int(input()))
c=input()
d={c=='even': (lambda x: x%2==0),c=='odd': lambda x: x%2!=0,c=='negative': (lambda x: x<0), c=='positive': (lambda x: x>=0) }

for i in l :
    if d[True](i)==True : k.append(i)

print(k)