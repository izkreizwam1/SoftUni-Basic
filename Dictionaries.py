# 02. Judge
d_con={}
d_user={}

def check_in_d(i,d):
    if i in d: return True
    else: return False
 while True:
    a=input()
    if a=="no more time": break
    user, con, point= a.split(' -> ')
    if check_in_d(con,d_con):
        if check_in_d(user,d_con[con]):
            d_con[con][user]=max(d_con[con][user],int(point))
        else: d_con[con][user]=int(point)
    else:
        d_con[con]={user: int(point)}

    if check_in_d(user,d_user):
        if check_in_d(con,d_user[user]):
            d_user[user][con]=max(d_user[user][con],int(point))
        else: d_user[user][con]=int(point)
    else:
        d_user[user]={con: int(point)}

for i in d_con:
    print(f"{i}: {len(d_con[i])} participants")
    n=0
    d_c_s=sorted(d_con[i].items(),key =lambda x: x[1],reverse=True)

    for j in d_c_s:
        n+=1
        print(f'{n}. {j[0]} <::> {j[1]}')
print('Individual standings:')
d_p={}
for i in d_user:
    d_p[i]=sum(d_user[i].values())
d_p = sorted(d_p.items(), key=lambda x: x[1], reverse=True)
n1=0
for i in d_p:
    n1+=1
    print(f'{n1}. {i[0]} -> {i[1]}')



# # 01. Ranking
# d_contest={}
# d_user={}
#
# while True:
#     a=input()
#     if a=="end of contests": break
#     d_contest[a.split(':')[0]]=a.split(':')[1]
#
# while True:
#     a=input()
#     if a == "end of submissions": break
#     a=a.split('=>')
#     if d_contest.get(a[0])==a[1]:
#         if a[2] in d_user:
#             try:
#                 d_user[a[2]][a[0]]=max(d_user[a[2]].get(a[0]),int(a[3]))
#             except:
#                 d_user[a[2]][a[0]]=int(a[3])
#         else:
#             d_user[a[2]]={}
#             d_user[a[2]][a[0]]=int(a[3])
#
# max=0
# max_u=''
# for i in d_user:
#     k=sum(d_user[i].values())
#     if max<k:
#         max=k
#         max_u=i
# print(f"Best candidate is {max_u} with total {max} points.\nRanking:")
# names= sorted(list(d_user.keys()))
# for i in names:
#     print(i)
#     sorted_d= sorted(d_user[i].items(), key=lambda x: x[1],reverse=True)
#     for j in sorted_d:
#        print(f'#  {j[0]} -> {j[1]}')

# # 11.	*SoftUni Exam Results
# d={}
# dl={}
#
# while True:
#     a=input()
#     if a=="exam finished": break
#     a=a.split('-')
#     if a[1]=='banned':
#         for k,v in d[a[0]].items():
#             d[a[0]][k]=None
#         continue
#     u,l,s=a
#     dl[l]=(lambda x : dl[x]+1 if bool(dl.get(x)) else 1)(l)
#     s=int(s)
#     if u not in d: d[u]={}
#     if bool(d[u].get(l)): d[u][l]=max(d[u][l],s)
#     else: d[u][l]=s
#
# print('Results:')
# for i in d:
#     for j in d[i]:
#         if d[i][j]!=None: print(f'{i} | {d[i][j]}')
#
# print('Submissions:')
# for k,v in dl.items():
#     print(f'{k} - {v}')



# 10.	*Force Book
# d={}
# def check(user,force):
#     for i in d:
#         if user in d[i]:
#             return 0
#     if force in d:
#         return 1
#     else: return 2
# def find_u(user):
#     for i in d:
#         if user in d[i]:
#             return [i,d[i].index(user)]
#
# while True:
#     # print(d)
#     a=input()
#     if '|' in a : c='|'
#     elif '->' in a : c='->'
#     a=a.split(f' {c} ')
#     if a[0]=="Lumpawaroo": break
#
#     if c=='|':
#         u,f =a[1],a[0]
#         if check(u,f)==0: continue
#         elif check(u,f)==1: d[f]=d[f]+[u]
#         elif check(u,f)==2: d[f]=[u]
#
#     elif c=='->':
#         u,f = a[0],a[1]
#         if check(u, f) == 0:
#             del d[find_u(u)[0]][find_u(u)[1]]
#
#
#         if check(u, f) == 1:
#             d[f] = d[f] + [u]
#             print(f"{u} joins the {f} side!")
#         elif check(u, f) == 2:
#             d[f] = [u]
#             print(f"{u} joins the {f} side!")
# for i in d:
#     if len(d[i])>0:
#         print(f"Side: {i}, Members: {len(d[i])}")
#         for j in d[i]:
#             print(f"! {j}")


# # 1.	Company Users
# d={}
# while True:
#     a=input()
#     if a=='End': break
#     a=a.split(' -> ')
#     if a[0] in d and a[1] in d[a[0]]:
#         continue
#     else:
#         if not bool(d.get(a[0])) : d[a[0]]=[a[1]]
#         else: d[a[0]]+=[a[1]]
# for i in d:
#     print(f"{i}")
#     for j in d[i]:
#         print(f"-- {j}")

# # 09. Student Academy
# d={}
# def check(i):
#     return +sum(d[i])/len(d[i])>=4.5
# n= int(input())
# for i in range(n):
#     a=input()
#     b=float(input())
#     if a not in d: d[a]=[b]
#     else: d[a]+=[b]
#
# # d=dict(map(lambda i,j: (i,j), a,b))
# s=dict(map(lambda i :  (i,sum(d[i])/len(d[i])) if check(i) else (0,1),d))
# # k=dict(map(lambda i :  (i,sum(d[i])/len(d[i]) if check(i) else None),d))
# if s.get(0): del s[0]
# for i in s:
#     print(f'{i} -> {s[i]:.2f}')

# # 08. Courses
# d={}
# while True:
#     a=input()
#     if a=='end': break
#     a, b=a.split(' : ')
#     if not bool(d.get(a)) : d[a]=[b]
#     else: d[a]=d[a]+[b]
# for i in d:
#     print(f"{i}: {len(d[i])}")
#     for j in d[i]:
#         print(f"-- {j}")

# # 07. SoftUni Parking
# n= int(input())
# d={}
# for i in range(n):
#     a=input().split(' ')
#     comand,user= a[0],a[1]
#     if comand=='register':
#         num=a[2]
#         if user in d: print(f"ERROR: already registered with plate number {num}")
#         else:
#             d[user]=num
#             print(f"{user} registered {num} successfully")
#     elif comand=='unregister':
#         if user in d:
#             print(f"{user} unregistered successfully")
#             del d[user]
#         else: print(f"ERROR: user {user} not found")
# for i in d:
#     print(f"{i} => {d[i]}")

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
# d=dict(map(lambda i,j: (i,j), a,b))
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