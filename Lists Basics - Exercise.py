# Seize the Fire
# a=input().split('#')
# b=int(input())
# e=0
# t=[]
# d={'High':list(range(81,126)),'Medium':list(range(51,81)),'Low':list(range(1,51))}
# a=list(map(lambda x: x.split(' = '),a))
# for i in range(len(a)):
#     if int(a[i][1]) not in d[a[i][0]]: continue
#     if int(a[i][1])<=b:
#         b-=int(a[i][1])
#         e+=0.25*int(a[i][1])
#         t.append(int(a[i][1]))
#
# print('Cells:\n')
# for i in t:
#     print(f' - {i}\n')
# print(f'Effort: {e:.2f}\n')
# print(f'Total Fire: {sum(t)}')


# # Easter Gifts
# a=input().split(' ')
# b=input()
# while b!="No Money" :
#     b=b.split(' ')
#     if b[0]=='OutOfStock':a=list(map(lambda x:x.replace(b[1],'None'),a))
#     if b[0]=='Required' and int(b[2])<len(a): a[int(b[2])]=b[1]
#     if b[0]=='JustInCase': a[-1]=b[1]
#     b=input()
# l=[i for i in a if i!='None']
# print(' '.join(l))

# # Survival of the Biggest
# a=input()
# b=int(input())
# l=[eval(x) for x in a.split(' ')]
# for i in range(b):
#     l.remove(min(l))
# print(l)

# a=input()
# b=int(input())
# l=a.split(' ')
# n=len(l)
# while b>0:
#     l1,l2=l[:int(n/2)],l[int(n/2):]
#     l=[]
#     for i in range(int(n/2)):
#         l+=l1[i]+l2[i]
#     b-=1
# print(l)

# a=input().split((', '))
# b= int(input())
# begger_list=[0]*b
# for i in range(len(a)):
#     begger_list[i%b]+=int(a[i])
# print(begger_list)


# a= input()
# b=int(input())
# l=[eval(i) for i in a.split(', ')]
# l+=(int((len(l)/b)+1)*b -len(l))*[0]
# k=[l[x:(x+b)] for x in range(0,len(l),b)]
# L=[sum(x) for x in zip(*k)]
# print(L)

# a=input()
# s= set(a.split(' '))
#
# print(f"Team A - {11-''.join(s).count('A')}; Team B - {11-''.join(s).count('B')}")
# if ''.join(s).count('A')>4 or ''.join(s).count('B')>4: print("Game was terminated")

# a,b = int(input()), int(input())
# l=[]
# for i in range(1,b+1): l.append(a*i)
# print(l)

# a=input()
# l=a.split(' ')
# for i in range(len(l)): l[i]=-int(l[i])
# print(l)
