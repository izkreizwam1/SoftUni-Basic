# 9.	*Anonymous Threat
a=input().split(' ')
def merge(a,start,end):
    if start>=len(a): return a
    if end>len(a): end=len(a)
    end+=1
    b=[''.join(a[start:end])]
    return a[0:start]+b+a[end:]

def divide(a,idx,parts):
    if idx>len(a)-1 : return a
    num_sym = len(a[idx]) // parts

    if len(a[idx])%parts==0 :
        b = [a[idx][i:i + num_sym] for i in range(0, len(a[idx]), num_sym)]
        return a[:idx]+b+a[idx+1:]
    else:
        b = [a[idx][i:i + num_sym] for i in range(0, len(a[idx]), num_sym)]
        b=b[:-2]+[b[-2]+b[-1]]
        return a[:idx] + b + a[idx + 1:]
command=input()
while command!='3:1':
    command=command.split(' ')
    if command[0]=='merge': a=merge(a,int(command[1]),int(command[2]))
    if command[0]=='divide': a=divide(a,int(command[1]),int(command[2]))
    command=input()
print(' '.join(a))



# #  8.	Decipher This!
# a=input().split(' ')
# a= [list(x) for x in a]
# num=[str(i) for i in range(10)]
# first=[]
# for i in a:
#     while i[0] in num:
#         if i[0] in num: first.append(i.pop(i.index(i[0])))
#     i[0],i[-1]=i[-1],i[0]
#     print(chr(int(''.join(first))),''.join(i), sep='', end=' ')
#     first=[]

# # Group of 10's
# a= [int(i) for i in input().split(', ')]
# m= max([(lambda x: x//10 if x%10==0 else (x//10+1))(x) for x in a])
# for i in range(1,m+1):
#     l=list(filter(lambda x: x<=i*10,a))
#     print(f"Group of {i*10}'s: {l}")
#     a=[x for x in a if (x not in l)]

# #  Electron Distribution
# # a=int(input())
# # n=1
# # l=[]
# # while a >= 2*(n**2):
# #     l.append(2*(n**2))
# #     a-=2*(n**2)
# #     n+=1
# # if a>0 : l.append(a)
# # print(l)
# a=int(input())
# l=[]
# while a>0:
#     n=len(l)+1
#     l.append(min(2*(n**2),a))
#     a-=2*(n**2)
# print(l)

# # 5.	Office Chairs
# rooms= ['']*int(input())
# free_ch=0
# c=0
# for i in range(len(rooms)):
#     m,n = input().split(' ')
#     if len(m)<int(n): print(f'{int(n)-len(m)} more chairs needed in room {i+1}')
#     else:
#         free_ch+=(len(m)-int(n))
#         c+=1
# if c==len(rooms): print(f'Game On, {free_ch} free chairs left')

# #4.	Number Classification
# a=input().split(', ')
# p=list(filter(lambda x: int(x)>=0,a))
# n=list(filter(lambda x: int(x)<0,a))
# e=list(filter(lambda x: int(x)%2==0,a))
# o=list(filter(lambda x: int(x)%2!=0,a))
# print(f'Positive: {", ".join(p)}')
# print(f'Negative: {", ".join(n)}')
# print(f'Even: {", ".join(e)}')
# print(f'Odd: {", ".join(o)}')

# # Word Filter
# a=input().split(' ')
# b= filter(lambda x: len(x)%2==0, a )
# print('\n'.join(b))

# # 2.	Next Version
# a=int(''.join(input().split('.')))
# print('.'.join(str(a+1)))

# # 1.	Which Are In?
# a=input().split(', ')
# b=input().split(', ')
# r=[]
# for i in a:
#     for j in b:
#         if i in j :
#             r.append(i)
#             break
# print(r)

# # The Office
# a= list(map(int,input().split(' ')))
# b=int(input())
# happy=list(filter(lambda x : x>=sum(a)/len(a),a))
# if len(happy)>=len(a)/2 : print(f'Score: {len(happy)}/{len(a)}. Employees are happy!')
# else: print(f'Score: {len(happy)}/{len(a)}. Employees are not happy!')

# #***************** Even Numbers ***********************************************************************
# a= input().split(', ')

# num_list = list(map(int,a))
# m1=map(lambda x: x if num_list[x]%2==0 else 'no',range(len(num_list)))
# print(list(filter(lambda x : x!='no',m1)))
# print([i for i in range(len(a)) if int(a[i])%2==0])
# def en(a):
#     l=[]
#     for k in a:
#         if int(k)%2==0:
#             l.append(a.index(k))
#     return l
# m=en(a)

# # m=[lambda k: a.index(k) for k in a if int(k)%2==0)]
# m=filter(lambda x: x!='az',[(lambda k: a.index(k) if int(k)%2==0 else 'az')(k) for k in a])
# # m=filter(lambda x: x!=None,[(lambda k: a.index(k) if int(k)%2==0 else None)(k) for k in a])
# # print([lambda a: a.index(k) for k in a if int(k)%2==0])
# print(list(m))



# # 5.	Sorting Names
# a= input().split(', ')
# print(sorted(a, key=lambda a : (-len(a),str.lower(a))))

# # 4.	Palindrome Strings
# a= input().split(' ')
# b=input()
# print([i for i in a if i==i[::-1]])
# print(f"Found palindrome {a.count(b)} times")

# # To-do List
# l=[0]*10
# while True:
#     a=input()
#     if a=='End': break
#     a=a.split('-')
#     l.pop(int(a[0])-1)
#     l.insert(int(a[0])-1, a[1])
# print([i for i in l if i !=0 ])

# Trains
# l=int(input())*[0]
# a=input()
# def add(add):
#     add=int(add[1])
#     global l
#     l[-1]+=add
# def insert(ins):
#     ins=ins[1:]
#     global l
#     ins=[int(i) for i in ins]
#     l[ins[0]]+=ins[1]
# def leave(leave):
#     leave=leave[1:]
#     global l
#     leave=[int(i) for i in leave]
#     l[leave[0]] -= leave[1]
#
# while a!='End' :
#     a=a.split(' ')
#     if a[0]=='add': add(a)
#     if a[0]=='insert': insert(a)
#     if a[0]=='leave': leave(a)
#     a=input()
# print(l)

# text = input()
# vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
# no_vowels = ''.join([x for x in text if x not in vowels])
# print(no_vowels)
