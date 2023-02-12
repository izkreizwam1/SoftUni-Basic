# # 6.	List Manipulator
# l=input().split(' ')
# l=[int(i) for i in l]
# #
# # def last_func(array, command_count, odd_or_even):
# #     if command_count > len(array) or command_count < 0:
# #         print("Invalid count")
# #     else:
# #         if odd_or_even == "even":
# #             all_even = []
# #             last_even = []
# #             for element in array:
# #                 if element % 2 == 0:
# #                     all_even.append(element)
# #             if len(all_even) > command_count:
# #                 count = command_count
# #                 for i in range(1, command_count + 1):
# #                     last_even.append(all_even[-count])
# #                     count -= 1
# #             else:
# #                 last_even = all_even
# #             print(last_even)
# #         elif odd_or_even == "odd":
# #             all_odd = []
# #             last_odd = []
# #             for element in array:
# #                 if element % 2 != 0:
# #                     all_odd.append(element)
# #             if len(all_odd) > command_count:
# #                 count = command_count
# #                 for i in range(1, command_count + 1):
# #                     last_odd.append(all_odd[-count])
# #                     count -= 1
# #             else:
# #                 last_odd = all_odd
# #             print(last_odd)
#
# def exchange(r,k):
#     r=[]
#     global l
#     r=l
#     k=int(k)
#     if k>=len(r) or k<0 :
#         print("Invalid index")
#         return
#     else :
#         r=r[k+1:]+r[:k+1]
#         l=r
#         return
#
# def maxeo(r,k):
#     if k=='odd': m=[i for i in r if i%2==1]
#     else: m=[i for i in r if i%2==0]
#     m.sort()
#     if m==[] : return print("No matches")
#     return print(len(r) - r[::-1].index(m[-1])-1)
# def mineo(r,k):
#     if k=='odd': m=[i for i in r if i%2==1]
#     else: m=[i for i in r if i%2==0]
#     m.sort()
#     if m == []: return print("No matches")
#     return print(len(r) - r[::-1].index(m[0])-1)
#
# def first(r,k):
#     k=k.split(' ')
#     if int(k[0])>len(r): return print("Invalid count")
#     if k[1]=='odd': m=[i for i in r if i%2==1]
#     else: m=[i for i in r if i%2==0]
#     return print(m[:int(k[0])])
#
# def last(r,k):
#     k=k.split(' ')
#     if int(k[0])>len(r) or int(k[0])<0: return print("Invalid count")
#     if k[1]=='odd': m=[i for i in r if i%2==1]
#     else: m=[i for i in r if i%2==0]
#     m=m[-int(k[0])::1]
#     return print(m)
#
# a=input()
# # 'exchange': exchange,
# d={'exchange': exchange, "max": maxeo, "min": mineo, "first": first, "last": last}
# while a!='end':
#     a=a.split(' ',1)
#     d[a[0]](l,a[1])
#     a=input()
#
# print(l)

# # 5.	Tic-Tac-Toe
#
# a= [input().split(' ')]+[input().split(' ')]+[input().split(' ')]
# k=0
# d={0:"Draw!",1:"First player won", 2:"Second player won"}
# for i in range(3):
#     if len(set(a[i]))==1 and a[i][0]=='1' : k=1
#     elif len(set(a[i]))==1 and a[i][0]=='2' : k=2
#     elif a[0][i]==a[1][i]==a[2][i]=='1': k=1
#     elif a[0][i]==a[1][i]==a[2][i]=='2': k=2
#
# if (len(set(a[i][i] for i in range(3)))==1 or len(set(a[i][2-i] for i in range(3)))==1) and a[1][1]=='1': k=1
# if (len(set(a[i][i] for i in range(3)))==1 or len(set(a[i][2-i] for i in range(3)))==1) and a[1][1]=='2': k=2
# print(d[k])


# # 4.	Josephus Permutation
# a= input().split(' ')
# b=int(input())
# b -= 1 # pop automatically skips the dead guy
# idx = b%len(a)
# k=[]
# while len(a) > 0:
#     k.append(int(a.pop(idx))) # kill prisoner at idx
#     if len(a)>0: idx = (idx + b) % len(a)
# print(str(k).replace(" ", ""))



# # 3.	Car Race
# a=input().split(' ')
# a=[int(i) for i in a]
# f,s = 0,0
# for i in range(0,int((len(a)-1)/2),1):
#     if a[i]==0 : f*=0.8
#     else : f+=a[i]
# for i in range(int(len(a)-1),int((len(a)-1)/2),-1):
#     if a[i]==0 : s*=0.8
#     else : s+=a[i]
# d={f<s:['left',f],f>=s:['right',s]}
# print(f"The winner is {d[True][0]} with total time: {d[True][1]:.1f}")

# # 2.	Messaging
# a=input().split(' ')
# a=list(a)
# a=[[int(i) for i in k] for k in a]
# b=list(input())
# t=''
#
# for i in range(len(a)):
#     t+=b[sum(a[i])%len(b)]
#     del b[sum(a[i])%len(b)]
# print(t)

# 1.	Zeros to Back
# a=input()
# k=[]
# c=0
# l=a.split(', ')
# l=[int(i) for i in l]
# while 0 in l:
#     l.remove(0)
#     c+=1
# # for i in range(len(l)):
# #     if l[i]!='0': k.append(l[i])
# # m=[int(x) for x in (k+c*['0'])]
# print(l+c*[0])

# import re
#
# a= input().split('|')
# a=list(map(lambda x : x.split('-'),a))
# e,m=100,100
#
# for i in range(len(a)):
#     q=a[i][0]
#     w=int(a[i][1])
#     if q=='rest':
#         if e+w>=100 :
#             print(f"You gained {100-e} energy.")
#             e=100
#         else:
#             e+=w
#             print(f"You gained {w} energy.")
#         print(f"Current energy: {e}.")
#     elif q=='order':
#         e-=30
#         if e>=0 :
#             m += w
#             print(f"You earned {w} coins.")
#         else:
#             e+=80
#             print("You had to rest!")
#     else:
#         if w<=m:
#             print(f"You bought {q}")
#             m-=w
#         else:
#             print(f"Closed! Cannot afford {q}.")
#             exit()
# print(f'Day completed!\nCoins: {m}\nEnergy: {e}')

# Hello, France
# a= input().split('|')
# b=float(input())
# a=list(map(lambda x: x.split('->'),a))
# d={'Clothes':50.00, 'Shoes':35.00, 'Accessories':20.50}
# k=[]
# o=0
# for i in range(len(a)):
#     t=a[i][0]
#     p=float(a[i][1])
#     if p> d[t]: continue
#     if p<=b:
#         k.append(round(p*1.4,2))
#         b-=p
#         o+=p
# for i in range(len(k)):
#     print(f'{k[i]:.2f}',end=' ')
# print(f'\nProfit: {o*0.4:.2f}')
# if (o*1.4+b)>=150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")

# # Seize the Fire
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
# print('Cells:')
# for i in t:
#     print(f' - {i}')
# print(f'Effort: {e:.2f}')
# print(f'Total Fire: {sum(t)}')


# # Easter Gifts
# a=input().split(' ')
# b=input()
# while b!="No Money" :
#     b=b.split(' ')
#     if b[0]=='OutOfStock':a=list(map(lambda x:x.replace(b[1],'None'),a))
#     if b[0]=='Required' and 0<=int(b[2])<len(a): a[int(b[2])]=b[1]
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
# l=[str(x) for x in l]
# print(', '.join(l))

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

#
# a= input()
# b=int(input())
# l=[eval(i) for i in a.split(', ')]
# l+=(int((len(l)/b)+1)*b -len(l))*[0]
# k=[l[x:(x+b)] for x in range(0,len(l),b)]
# L=[sum(x) for x in zip(*k)]
# print(L)

# a=input()
# a=list(set(a.split(' ')))
# ac=0
# bc=0
# for i in range(len(a)):
#     if a[i][0]=='A': ac+=1
#     else :bc+=1
#     if ac>4 or bc>4 : break
# print(f"Team A - {11-ac}; Team B - {11-bc}")
# if ac>4 or bc>4 : print("Game was terminated")

# a,b = int(input()), int(input())
# l=[]
# for i in range(1,b+1): l.append(a*i)
# print(l)

# a=input()
# l=a.split(' ')
# for i in range(len(l)): l[i]=-int(l[i])
# print(l)
