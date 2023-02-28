# # 6.	Orders
# d={}
# while True:
#     a = input().split(' ')
#     if a[0]=='buy': break
#     a[1] = float(a[1])
#     a[2] = int(a[2])
#     if a[0] in d:
#         d[a[0]][0]=a[1]
#         d[a[0]][1]+=a[2]
#     else: d[a[0]]=[a[1],a[2]]
# for i in d:
#     print(f'{i} -> {d[i][0]*d[i][1]:.2f}')

# # 5.	Legendary Farming
# d={'shards':0,'fragments':0,'motes': 0}
# t={'shards':'Shadowmourne','fragments':'Valanyr','motes':'Dragonwrath'}
# flag=True
# while flag:
#     a=input().split(' ')
#     a=list((lambda i : int(a[i]) if i%2==0 else a[i].lower())(i) for i in range(len(a)))
#
#     for i in range(0,len(a),2):
#         if a[i+1] not in d: d[a[i+1]]=a[i]
#         else: d[a[i+1]]+=a[i]
#         if d['shards']>=250 or d['fragments']>=250 or d['motes']>=250:
#             flag=False
#             win=a[i+1]
#             d[win]-=250
#             break
#
#
# print(f"{t[win]} obtained!")
# print(f'shards: {d.pop("shards")}\nfragments: {d.pop("fragments")}\nmotes: {d.pop("motes")}')
# for i in d:
#     print(f'{i}: {d[i]}')



# #  4.	Phonebook
# d={}
# while True:
#     a=input()
#     if '-' not in a: break
#     a=a.split('-')
#     d[a[0]]=a[1]
#
# for i in range(int(a)):
#     c= input()
#     if c in d :
#         print(f'{c} -> {d[c]}')
#     else: print(f"Contact {c} does not exist.")

# #  Capitals
# a=input().split(', ')
# b=input().split(', ')
# # d=dict(map(lambda i,j: (i,j), a,b))
# d=dict(zip(a,b))
# for i in d:
#     print(f'{i} -> {d[i]}')

# A Miner Task
# d={}
# while True:
#     a=input()
#     if a=='stop': break
#     b=int(input())
#     d[a]=b+ [0 if d.get(a)==None else d[a]][0]
# for i in d:
#     print(f'{i} -> {d[i]}')

# a=''.join(input().split(' '))
# d={i: 0 for i in a}
# for i in a:
#     d[i]+=1
# for i in d:
#     print(f'{i} -> {d[i]}')

# Dictionaries - Lab ######
# n=int(input())
# d={}
# for i in range(n):
#     a=input()
#     if a not in d:
#         d[a]=[]
#     d[a].append(input())
# for i in d:
#     print(f'{i} - {", ".join(d[i])}')

# a=[i.lower()  for i in input().split(' ')]
# d={(i if a.count(i)%2!=0 else None):(a.count(i) if a.count(i)%2!=0 else None) for i in a}
# if None in d: del d[None]
# print(' '.join(d.keys()))

# a=input().split(', ')
# d={word: ord(word) for word in a}
# print(d)

# a=input()
# d={}
# while ':' in a:
#     name,num,c=a.split(':')
#     if c not in d:
#         d[c]=[f'{name} - {num}']
#     else: d[c].append(f'{name} - {num}')
#     a=input()
# a=' '.join(a.split('_'))
# print('\n'.join(d[a]))

# d={}
# while True:
#     a=input().split(': ')
#     if a[0]=='statistics': break
#     if a[0] in d : d[a[0]]+=int(a[1])
#     else: d[a[0]]=int(a[1])
# print('Products in stock:')
# for x,y in d.items():
#     print(f'- {x}: {y}')
# print(f'Total Products: {len(d)}\nTotal Quantity: {sum(d.values())}')

# a=input().split(' ')
# d={}
# for i in range(0,len(a),2):
#     d[a[i]]=int(a[i+1])
# b=input().split(' ')
# for i in b:
#     if i in d:
#         print(f"We have {d[i]} of {i} left")
#     else: print(f"Sorry, we don't have {i}")

# a=input().split(' ')
# d={}
# for i in range(0,len(a),2):
#     d[a[i]]=int(a[i+1])
# print(d)