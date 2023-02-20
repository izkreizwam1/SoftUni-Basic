# # Dots
# from collections import Counter
#
# n=int(input())
# dot=[]
# t_final=0
#
#
# for i in range(n):
#     dot.append(list((lambda x: 1 if x=='.' else 0)(x) for x in input().split(' ')))
# # print(dot)
# def find_dots(dot,i):
#     flag=False
#     broi=0
#     pos=[]
#     pos_reserve=[]
#     if 1 in dot[i]:
#         pos = [dot[i].index(1)]
#         pos_reserve=[]
#         broi+=1
#         dot[i][pos[-1]]=0
#         for j in range(pos[-1]+1,len(dot[i])):
#             if dot[i][j]==1 and flag==False:
#                 pos.append(j)
#                 broi += 1
#                 dot[i][pos[-1]] = 0
#
#             elif dot[i][j]==0 :
#                 flag=True
#             elif dot[i][j]==1 and flag:
#                 pos_reserve.append(j)
#
#
#     return broi,pos,pos_reserve
#
# def add_reserve(dot,i,reserve_old,l):
#     c=list((Counter(reserve_old) & Counter(l)).elements())
#     for j in range(len(c)):
#         dot[i-1][c[j]]=0
#     return len(c)
#
#
#
# def check_sum():
#     i = 0
#     t=0
#     l_old=[]
#     reserve_old=[]
#     while i <n:
#         num,l,reserve = find_dots(dot,i)
#         if bool(l) and not bool(l_old):
#             t+=num
#             l_old=l
#             if reserve : reserve_old = reserve
#
#         elif bool(l) and bool(l_old):
#             if any(i in l_old for i in l):
#                 t+=num
#                 l_old=l
#                 # print(dot,reserve,reserve_old)
#                 if any(i in reserve_old for i in l):
#                     t+= add_reserve(dot,i,reserve_old,l)
#
#                     reserve_old=reserve
#                 else:
#                     reserve_old=reserve
#
#             else:
#                 break
#         elif not bool(l) and bool(l_old):
#             break
#         elif not bool(l) and not bool(l_old):
#             pass
#         i+=1
#     return t
#
#
# for i in range(n):
#     if sum(dot[i])>0:
#         t_final=max(t_final,check_sum())
# print(t_final)





# # Battle Ships
# n=int(input())
# mapi=[]
# t=0
# for i in range(n):
#     mapi.append(list((lambda x: int(x))(x) for x in input().split(' ')))
#
# hit=input().split(' ')
# for i in range(len(hit)):
#     hit[i]=hit[i].split('-')
#     hit[i]=list((map(lambda j: int(j),hit[i])))
#
# for i in range(len(hit)):
#     if mapi[hit[i][0]][hit[i][1]]>0:
#         mapi[hit[i][0]][hit[i][1]]-=1
#         if mapi[hit[i][0]][hit[i][1]]==0 : t+=1#
# print(t)

# Kate's Way Out ******************************************************************************************************************
# def check_path(kate,l1pos,l2pos):
#     kate=[pos]
#     for i in range(len(l1pos)):
#         if (min(kate)-1) in l1pos: kate.append(min(kate)-1)
#         if (max(kate) + 1) in l1pos: kate.append(max(kate) + 1)
#     l2pos=list(filter(None, [(lambda x: x if x in kate else None)(x) for x in l2pos]))
#     return l2pos
#
# def move(k,l2pos):
#     steps=max([(lambda x: abs(k-x))(x) for x in l2pos])
#     for i in l2pos:
#         if abs(k-i)==steps: k=i
#     return [k,steps+1]
#
#
# a=int(input())
# maze=[[] for i in range(a)]
# trip=0
# trip_down=0
# trip_up=0
#
# k=[]
# end_down=True
# end_up=True
# end=0
# p=[[] for i in range(a)]
# # find free spaces in maze and put in p and locate k
# for i in range(a):
#     maze[i].extend([j for j in input()])
#     for j in range(len(maze[i])):
#         if maze[i][j]=='k':
#             k=[i,j]
#         if maze[i][j]==' ':
#             p[i].extend([j])
#
# #  check for a way out
# for i in range(k[0],len(maze)):
#     if ' ' not in maze[i]:
#         end_down=False
# for i in range(k[0]-1,0-1,-1):
#     if ' ' not in maze[i]:
#         end_up=False
#
#
# # way down
# if end_down:
#     row = k[0]
#     pos = k[1]
#     for i in range(row,len(p)-1):
#         next_row=check_path(k,p[i],p[i+1])
#         pos, steps = move(pos,next_row)
#         trip_down+=steps
#         print(steps)
# # way up
# if end_up:
#     row = k[0]
#     pos = k[1]
#     for i in range(row-1,-1,-1):
#         next_row=check_path(pos,p[i+1],p[i])
#         pos, steps = move(pos,next_row)
#         trip_up+=steps
#         print(steps)
# if end_up==end_down==False: print('Kate cannot get out')
# else :
#     trip=max(trip_up,trip_down)
#     print(f'Kate got out in {trip+1} moves')


# # 2.	Take/Skip Rope
# a=[i for i in input()]
# n_list= [str(i) for i in range(10)]
# num=list(filter(lambda x: type(x)==int,[(lambda x: int(x) if x in n_list else x)(x) for x in a]))
# chars=list(filter(lambda x: type(x)!=int,[(lambda x: int(x) if x in n_list else x)(x) for x in a]))
# n_take, n_skip = [num[i] for i in range(0,len(num),2)],[num[i] for i in range(1,len(num),2)]
# l=[]
# for i in range(len(n_take)):
#     l.extend(chars[:n_take[i]])
#     del chars[:n_skip[i]+n_take[i]]
# print(''.join(l))

# # 1.	Social Distribution
# a=[int(x) for x in input().split(', ')]
# b=int(input())
# for i in range(len(a)):
#     a_sorted = sorted(a)
#     a_max_idx = a.index(a_sorted[-1])
#     if a[i]<b and a[a_max_idx]>=2*b-a[i]:
#         a[a_max_idx] -= (b - a[i])
#         a[i]+=b-a[i]
# if min(a)<b: print('No equal distribution possible')
# else: print(a)

# # SoftUni Course Planning
# a= input().split(', ')
#
# def check(a,title):
#     if title in a: return True
#     else: return False
#
#
# while True:
#     command=input()
#     if command=="course start" : break
#     command=command.split(':')
#     if command[0]=='Add':
#         if check(a,command[1])==False:
#             a.append(command[1])
#         # print(a)
#     elif command[0]=='Insert':
#         if check(a, command[1])==False:
#             a.insert(int(command[2]),command[1])
#         # print(a)
#     elif command[0]=='Remove':
#         if check(a, command[1]):
#             a.remove(command[1])
#         if check(a, command[1]+'-Exercise'):
#             a.remove(command[1]+'-Exercise')
#         # print(a)
#     elif command[0]=='Swap':
#         if check(a, command[1]) and check(a,command[2]):
#             slot1, slot2 = a.index(command[1]), a.index(command[2])
#             a[slot1], a[slot2] = a[slot2], a[slot1]
#             # print('swap main= ',a)
#         else: continue
#         if check(a, command[1] + '-Exercise'):
#             slot3=a.index(command[1] + '-Exercise')
#             ex_to_move= a.pop(slot3)        #test here
#             a.insert(slot2+1, ex_to_move)
#             # print('swap ex 1=',a)
#         if check(a, command[2] + '-Exercise'):
#             slot4 = a.index(command[2] + '-Exercise')
#             ex_to_move2 = a.pop(slot4)
#             a.insert(slot1+1, ex_to_move2)
#     #         # print('swap ex 2=',a)
#         # print(a)
#     elif command[0]=='Exercise':
#         if check(a, command[1]) :
#             if check(a, command[1]+'-Exercise') :
#                 continue
#             else:
#                 a.insert(a.index(command[1])+1, command[1]+'-Exercise')
#         else:
#             a.extend([command[1]])
#             # print('add course=',a)
#             a.extend([command[1] + '-Exercise'])
#         #     print('add ex=',a)
#
# for i in range(len(a)):
#     print(f'{i+1}.{a[i]}')

# # 10.	*Pokemon Don't Go
# import random
# input_list=[int(x) for x in input().split(' ')]
# total=0
# while len(input_list)>0:
#     value=random.randint(0,9)
#     idx=int(input())
#     if idx<0:
#         value=input_list[0]
#         input_list[0]=input_list[-1]
#     elif idx>=len(input_list):
#         value=input_list[-1]
#         input_list[-1]=input_list[0]
#     else:
#         value=input_list.pop(idx)
#     total+=value
#     input_list = [(lambda x: x + value if x <= value else x - value)(x) for x in input_list]
# print(total)

# # 9.	*Anonymous Threat
# a=input().split(' ')
# def merge(a,start,end):
#     if start>=len(a): return a
#     if start<0 : start=0
#     if end>len(a): end=len(a)
#     end+=1
#     b=[''.join(a[start:end])]
#     return a[:start]+b+a[end:]
#
# def divide(a,idx,parts):
#     num_sym = len(a[idx]) // parts
#
#     if len(a[idx])%parts==0 :
#         b = [a[idx][i:i + num_sym] for i in range(0, len(a[idx]), num_sym)]
#         return a[:idx]+b+a[idx+1:]
#     else:
#         b = [a[idx][i:i + num_sym] for i in range(0, len(a[idx]), num_sym)]
#         b=b[:-2]+[b[-2]+b[-1]]
#         return a[:idx] + b + a[idx + 1:]
# command=input()
# while command!='3:1':
#     command=command.split(' ')
#     if command[0]=='merge': a=merge(a,int(command[1]),int(command[2]))
#     if command[0]=='divide': a=divide(a,int(command[1]),int(command[2]))
#     command=input()
# print(' '.join(a))



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
