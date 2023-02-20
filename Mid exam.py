# # 3.	Memory Game
# a=input().split(' ')
# step=0
# def check_idx(idx1,idx2):
#     return (0<=idx1<len(a) and 0<=idx2<len(a) and idx1!=idx2)
#
#
# while True:
#     com=input()
#     if com=='end': break
#     step+=1
#     com=com.split(' ')
#     com=[int(x) for x in com]
#     idx1,idx2 = com[0],com[1]
#     if not check_idx(idx1,idx2):
#         a.insert(int(len(a)/2),f"-{step}a" )
#         a.insert(int(len(a)/2),f"-{step}a" )
#         print("Invalid input! Adding additional elements to the board")
#     elif check_idx(idx1,idx2) and a[idx1]==a[idx2]:
#         el=a.pop(idx1)
#         a.remove(el)
#         print(f"Congrats! You have found matching elements - {el}!")
#     elif check_idx(idx1,idx2) and a[idx1]!=a[idx2]:
#         print("Try again!")
#     if len(a)==0 :
#         print(f"You have won in {step} turns!")
#         break
#
# if len(a)>0:
#     print(f"Sorry you lose :(\n{' '.join(a)}")



# MuOnline
# a=input().split('|')
# h=100
# b=0
#
# for i in range(len(a)):
#     com=a[i].split(' ')
#     if com[0]=='potion':
#         h1=100-h
#         h=min(h+int(com[1]),100)
#         print(f"You healed for {min(h1,int(com[1]))} hp.")
#         print(f"Current health: {h} hp.")
#     elif com[0]=='chest':
#         b+=int(com[1])
#         print(f"You found {int(com[1])} bitcoins.")
#     else:
#         h-=int(com[1])
#         if h<=0:
#             print(f"You died! Killed by {com[0]}.")
#             print(f"Best room: {i+1}")
#             break
#         else: print(f"You slayed {com[0]}.")
# if h>0: print(f"You've made it!\nBitcoins: {b}\nHealth: {h}")

# # 1.	Black Flag
# a=int(input())
# b=int(input())
# c=float(input())
# total=0
# for i in range(1,a+1):
#     total+=b
#     if i%3==0: total+=0.5*b
#     if i%5==0: total*=0.7
# if total>=c: print(f"Ahoy! {total:.2f} plunder gained.")
# else: print(f"Collected only {(total/c)*100:.2f}% of the plunder.")

# # Man O War
# ship = [int(x) for x in input().split('>')]
# enemy = [int(x) for x in input().split('>')]
# maxi = int(input())
# flag = True
#
# while flag:
#     command = input()
#     if command == 'Retire': break
#     command = command.split(' ')
#     if command[0] == 'Fire' and 0 <= int(command[1]) < len(enemy):
#         enemy[int(command[1])] -= int(command[2])
#         if enemy[int(command[1])] <= 0:
#             print("You won! The enemy ship has sunken.")
#             flag = False
#
#     elif command[0] == 'Defend' and 0 <= int(command[1]) < len(ship) and 0 <= int(command[2]) < len(ship):
#         if int(command[1]) <= int(command[2]):
#             for i in range(int(command[1]), int(command[2]) + 1):
#                 ship[i] -= int(command[3])
#                 if ship[i] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     flag = False
#                     break
#     elif command[0] == 'Repair' and 0 <= int(command[1]) < len(ship):
#         ship[int(command[1])] += int(command[2])
#         if ship[int(command[1])] > maxi: ship[int(command[1])] = maxi
#     elif command[0] == 'Status':
#         bad = maxi / 5
#         repair = len(list(filter(lambda x: x < bad, ship)))
#         print(f"{repair} sections need repair.")
#
# if flag:
#     ship_s = sum(list(filter(lambda x: x <= maxi, ship)))
#     enemy_s = sum(list(filter(lambda x: x <= maxi, enemy)))
#     print(f"Pirate ship status: {ship_s}\nWarship status: {enemy_s}")

# #  Shopping List
# a= input().split('!')
#
# def check(a,title):
#     if title in a: return True
#     else: return False
#
#
# while True:
#     command=input()
#     if command=="Go Shopping!" : break
#     command=command.split(' ')
#     if command[0]=='Urgent':
#         if check(a,command[1])==False:
#             a.insert(0,command[1])
#         # print(a)
#     elif command[0]=='Correct':
#         if check(a, command[1])==True:
#             idx= a.index(command[1])
#             a.pop(idx)
#             a.insert(idx,command[2])
#         # print(a)
#     elif command[0]=='Unnecessary':
#         if check(a, command[1]):
#             a.remove(command[1])
#         if check(a, command[1]+'-Exercise'):
#             a.remove(command[1]+'-Exercise')
#         # print(a)
#     elif command[0]=='Rearrange':
#         if check(a, command[1]):
#             idx = a.index(command[1])
#             slot1=a.pop(idx)
#             a.append(slot1)
#             # print('swap main= ',a)
#
#         #     print('add ex=',a)
#
#
# print(', '.join(a))

# # 1.	Bonus Scoring System
# import math
#
# a=int(input())
# b=int(input())
# bonus=int(input())
#
# max_at=0
# for i in range(a):
#     at=int(input())
#     max_at=max(at,max_at)
# t=0
# if b!=0:
#     t=math.ceil((max_at/b)*(5+bonus))
# print(f'Max Bonus: {t}.')
# print(f'The student has attended {max_at} lectures.')