# # Messages Manager
# n= int(input())
# d={}
#
# while True:
#     b= input()
#     if b=='Statistics': break
#     b=b.split('=')
#     if b[0]=='Add':
#         if b[1] in d: continue
#         d[b[1]]=[int(b[2]),int(b[3])]
#
#     elif b[0]=='Message':
#         if b[1] in d and b[2] in d:
#             d[b[1]][0]+=1
#             if sum(d[b[1]])>=n :
#                 del d[b[1]]
#                 print(f"{b[1]} reached the capacity!")
#             d[b[2]][1]+=1
#             if sum(d[b[2]])>=n :
#                 del d[b[2]]
#                 print(f"{b[2]} reached the capacity!")
#
#     elif b[0]=='Empty':
#         if b[1]=='All': d={}
#         elif b[1] in d : del d[b[1]]
#
# print(f"Users count: {len(d)}")
# for i in d:
#     print(f'{i} - {sum(d[i])}')
#
# #  Message Translator
# import re
# n=int(input())
# r=r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'
# for i in range(n):
#     a=input()
#     t=re.findall(r,a)
#     if bool(t):
#         print(t[0][0],end=': ')
#         for j in t[0][1]:
#             print(f'{ord(j)}', end=' ')
#         print('')
#     else:
#         print("The message is invalid")
#
# # Decrypting Commands
# a= input()
#
# while True:
#     b= input()
#     if b=='Finish': break
#     b=[int(x) if x.isdigit() else x for x in b.split()]
#     # print(b)
#     if b[0]=='Replace' :
#         a=a.replace(b[1],b[2])
#         print(a)
#     elif b[0]=='Cut' :
#         if 0<=int(b[1])<len(a) and 0<=int(b[2])<len(a):
#             a=a[:b[1]]+a[b[2]+1:]
#             print(a)
#         else:
#             print('Invalid indices!')
#     elif b[0]=='Make' :
#         if b[1]=='Upper':
#             a=a.upper()
#         elif b[1]=='Lower':
#             a=a.lower()
#         print(a)
#     elif b[0]=='Check' :
#         if b[1] in a:
#             print(f"Message contains {b[1]}")
#         else: print(f"Message doesn't contain {b[1]}")
#     elif b[0]=='Sum' :
#         if 0<=int(b[1])<len(a) and 0<=int(b[2])<len(a):
#             sum=0
#             for i in a[b[1]:b[2]+1]:
#                 sum+=ord(i)
#
#         else:
#             print('Invalid indices!')
#             continue
#
#         print(sum)


# # P!rates
#
# d={}
# while True:
#     a=input()
#     if a=='Sail': break
#     c,p,g=[int(x) if x.isdigit() else x for x in a.split('||')]
#     if c in d:
#         d[c][0]+=p
#         d[c][1]+=g
#     else:
#         d[c]=[p,g]
# while True:
#     b=input()
#     if b=='End': break
#     command,c,*info=[int(x) if x.isdigit() else x for x in b.split('=>')]
#     if command=='Plunder':
#         p,g=info
#         d[c][0]-=p
#         d[c][1]-=g
#         print(f"{c} plundered! {g} gold stolen, {p} citizens killed.")
#         if d[c][0]==0 or d[c][1]==0:
#             del d[c]
#             print(f"{c} has been wiped off the map!")
#
#     elif command=='Prosper':
#         info=int(info[0])
#         if info<0 :
#             print("Gold added cannot be a negative number!" )
#         else:
#             d[c][1]+=info
#             print(f"{info} gold added to the city treasury. {c} now has {d[c][1]} gold.")
# if len(d)==0 :
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")
# else:
#     print(f"Ahoy, Captain! There are {len(d)} wealthy settlements to go to:")
#     for i in d:
#         print(f'{i} -> Population: {d[i][0]} citizens, Gold: {d[i][1]} kg')

# # Emoji Detector
# import re
#
# a= input()
# r=r'(\*\*|::)(?P<word>[A-Z][a-z]{2,})\1'
# th=1
# for i in a:
#     if i.isdigit(): th*=int(i)
#
# print(f"Cool threshold: {th}")
# t=re.finditer(r,a)
# t1=re.findall(r,a)
# print(f"{len(t1)} emojis found in the text. The cool ones are:")
#
# for i in t1:
#     k=0
#     for j in i[1]:
#        k+=ord(j)
#     if k>=th: print(i[0]+i[1]+i[0])

# Activation Keys
# a= input()
#
# while True:
#     b=input()
#     if b=='Generate': break
#     b=b.split('>>>')
#     if b[0]=='Contains':
#         if b[1] in a :
#             print(f"{a} contains {b[1]}")
#         else: print("Substring not found!")
#     elif b[0]=='Flip':
#         k=''
#         b2=int(b[2])
#         b3=int(b[3])
#         for i in a[b2:b3]:
#             if b[1]=='Lower': k+=i.lower()
#             elif b[1]=='Upper': k+=i.upper()
#             else:k+=i
#         a=a[:b2]+k+a[b3:]
#         print(a)
#     elif b[0]=='Slice':
#         a=a[:int(b[1])]+a[int(b[2]):]
#         print(a)
# print(f"Your activation key is: {a}")

# # Heroes of Code and Logic VII
# n= int(input())
# d={}
# for i in range(n):
#     name,hp,mp =input().split()
#     d[name]=[int(hp),int(mp)]
#
# while True:
#     b=input()
#     if b=='End': break
#     command, name , *info = [int(x) if x.isdigit() else x for x in b.split(' - ')]
#     if command=='CastSpell':
#         mp, spell = info
#         if mp<=d[name][1]:
#             d[name][1]-=mp
#             print(f"{name} has successfully cast {spell} and now has {d[name][1]} MP!")
#         else: print(f"{name} does not have enough MP to cast {spell}!")
#
#     elif command=='TakeDamage':
#         dam, att = info
#         d[name][0]-=dam
#         if d[name][0]>0:
#             print(f"{name} was hit for {dam} HP by {att} and now has {d[name][0]} HP left!")
#         else:
#             del d[name]
#             print(f"{name} has been killed by {att}!")
#     elif command=='Recharge':
#         re=info[0]
#         if d[name][1]+re>200:
#             re=200-d[name][1]
#             d[name][1]=200
#         else:  d[name][1]+=re
#         print(f"{name} recharged for {re} MP!")
#     elif command=='Heal':
#         re=info[0]
#         if d[name][0] + re > 100:
#             re = 100 - d[name][0]
#             d[name][0] = 100
#         else:
#             d[name][0] += re
#         print(f"{name} healed for {re} HP!")
# for i in d:
#     print(f'{i}\n  HP: {d[i][0]}\n  MP: {d[i][1]}')


# # Fancy Barcodes
# import re
#
# n=int(input())
# r=r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'
#
# for i in range(n):
#     a=input()
#     found_barcode=re.findall(r,a)
#
#     if found_barcode :
#         group=''
#         for j in found_barcode[0]:
#             if j.isdigit():
#                 group+=j
#         if group=='': group='00'
#         print(f'Product group: {group}')
#     else:print("Invalid barcode")

# Password Reset
# a=input()
#
# while True:
#     b=input()
#     if b=='Done': break
#     b=b.split()
#     if b[0]=='TakeOdd':
#         a=a[1::2]
#         print(a)
#     elif b[0]=='Cut':
#         a=a[:int(b[1])]+a[int(b[1])+int(b[2]):]
#         print(a)
#     elif b[0]=='Substitute':
#         if b[1]in a:
#             a=a.replace(b[1],b[2])
#             print(a)
#         else: print("Nothing to replace!")
# print(f"Your password is: {a}")

# Need for Speed III
# n= int(input())
# d={}
# for i in range(n):
#     a=input().split('|')
#     d[a[0]]=[int(a[1]), int(a[2])]
#
# while True:
#     b=input()
#     if b=='Stop': break
#     b=b.split(' : ')
#     car=b[1]
#     if b[0]=='Drive':
#         if d[car][1]<int(b[3]) :
#             print("Not enough fuel to make that ride")
#
#         else:
#             d[car][0]+=int(b[2])
#             d[car][1]-=int(b[3])
#             print(f"{car} driven for {b[2]} kilometers. {b[3]} liters of fuel consumed.")
#             if d[car][0]>=100000:
#                 del d[car]
#                 print(f"Time to sell the {car}!")
#     elif b[0]=='Refuel':
#         f=min(75-d[car][1], int(b[2]))
#         d[car][1]=min(75, d[car][1]+int(b[2]))
#         print(f"{car} refueled with {f} liters")
#     elif b[0]=='Revert':
#         d[car][0]-=int(b[2])
#         if d[car][0]<10000:
#             d[car][0]=10000
#             continue
#         print(f"{car} mileage decreased by {b[2]} kilometers")
# for i in d:
#     print(f"{i} -> Mileage: {d[i][0]} kms, Fuel in the tank: {d[i][1]} lt.")


# # Mirror words
# import re
# a=input()
# l=[]
# r=r'(@|#)(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1'
# t=re.findall(r,a)
# pairs=len(t)
# for i in t:
#     if i[1]==i[2][::-1]:
#         l.append(f'{i[1]} <=> {i[2]}')
# if pairs:
#     print(f"{pairs} word pairs found!")
# else: print("No word pairs found!")
# if l :
#     print(f"The mirror words are:\n {', '.join(l)}")
# else: print("No mirror words!")

# # Secret Chat
# a=input()
# while True:
#     b=input()
#     if b=='Reveal': break
#     b=b.split(':|:')
#     if b[0]=='InsertSpace':
#         a=a[:int(b[1])]+' '+a[int(b[1]):]
#         print(a)
#     elif b[0]=='Reverse':
#         if b[1] in a:
#             a=a.replace(b[1],'',1)+b[1][len(b[1])::-1]
#             print(a)
#         else: print('error')
#     elif b[0]=='ChangeAll':
#         a=a.replace(b[1],b[2])
#         print(a)
# print(f"You have a new text message: {a}")

# Plant Discovery
# def rate(p,r,di):
#     if p in di:
#         di[p]['rate'].append(int(r))
#         return di
#     else:
#         print('error')
#         return di
# def update(p,r,di):
#     if p in di:
#         di[p]['rarity']=int(r)
#         return di
#     else:
#         print('error')
#         return di
# def reset(p,di):
#     if p in di:
#         di[p]['rate']=[]
#         return di
#     else:
#         print('error')
#         return di
#
# n= int(input())
# d={}
# for i in range(n):
#     a=input().split('<->')
#     d[a[0]]={'rarity':a[1], 'rate':[]}
#
# while True:
#     b=input()
#     if b=='Exhibition': break
#     command, data=b.split(': ')
#
#     if command=='Rate':
#         plant, x = data.split(' - ')
#         d=rate(plant, x,d)
#     elif command=='Update':
#         plant, x = data.split(' - ')
#         d=update(plant,x,d)
#     elif command=='Reset':
#         d=reset(data,d)
# print('Plants for the exhibition:')
# for i in d:
#     if d[i]['rate']==[]: k=0
#     else: k=(sum(d[i]["rate"])/len(d[i]["rate"]))
#     print(f'- {i}; Rarity: {d[i]["rarity"]}; Rating: {k:.2f}')



# # Destination Mapper
# import re
# a= input()
# r=r'([\/=])([A-Z][A-Za-z][A-Za-z]+)\1'
#
# t=re.findall(r,a)
# l=[]
# lt=0
# for i in t:
#     l.append(i[1])
#     lt+=len(i[1])
#
# # list_result = []
# # result = re.finditer(pattern, main_string)
# # total_travel_points = 0
# # for show in result:
# #     total_travel_points += len(show["location"])
# #     list_result.append(show["location"])
#
# print(f"Destinations: {', '.join(l)}")
# print(f"Travel Points: {lt}")

# # World Tour
# a=input()
#
# while True:
#     b=input()
#     if b=='Travel': break
#     command, x, y=b.split(':')
#     if command=='Add Stop':
#         x= int(x)
#         if x<len(a):
#             a=a[:x]+y+a[x:]
#         print(a)
#     elif command=='Remove Stop':
#         x, y =int(x), int(y)
#         if x<len(a) and y<len(a):
#             a=a[:x]+a[y+1:]
#         print(a)
#     elif command=='Switch':
#         a=a.replace(x,y)
#         print(a)
# print(f"Ready for world tour! Planned stops: {a}")

# # The Pianist
# def add(p,c,k,d):
#     if p in d:
#         print(f"{p} is already in the collection!")
#         return d
#     else:
#         d[p]=[c,k]
#         print(f"{p} by {c} in {k} added to the collection!")
#         return d
#
# def remove(p,d):
#     if p in d:
#         del d[p]
#         print(f"Successfully removed {p}!")
#         return d
#     else:
#         print(f"Invalid operation! {p} does not exist in the collection.")
#         return d
#
# def change(p,k,d):
#     if p in d:
#         d[p][1]=k
#         print(f"Changed the key of {p} to {k}!")
#         return d
#     else:
#         print(f"Invalid operation! {p} does not exist in the collection.")
#         return d
#
#
# n= int(input())
# di={}
# for i in range(n):
#     a= input().split('|')
#     di[a[0]]=[a[1],a[2]]
# while True:
#     b=input()
#     if b=='Stop': break
#     b=b.split('|')
#     if b[0]=='Add':
#         di=add(b[1],b[2],b[3],di)
#     elif b[0]=='Remove':
#         di=remove(b[1],di)
#     elif b[0]=='ChangeKey':
#         di=change(b[1],b[2],di)
#
# for i in di:
#     print(f"{i} -> Composer: {di[i][0]}, Key: {di[i][1]}")

# # Ad Astra
# import re
# c_total=0
#
# a=input()
# r=r'([#|])(?P<item>[A-Za-z\ ]+)\1(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<call>[0-9]{1,5})\1'
# t= re.finditer(r,a)
# for i in t:
#     # print(i)
#     c_total+=int(i['call'])
# print(f"You have food to last you for: {c_total//2000} days!")
# # print(t)
# t= re.finditer(r,a)
# for k in t:
#     print(f"Item: {k['item']}, Best before: {k['date']}, Nutrition: {k['call']}")
# # print(t)

# #  The Imitation Game
# a=input()
#
#
# while True:
#     b=input()
#     if b=='Decode': break
#     b=b.split('|')
#     if b[0]=='Move':
#         a=a[int(b[1]):]+a[:int(b[1])]
#     elif b[0]=='Insert':
#         a=a[:int(b[1])]+b[2]+a[int(b[1]):]
#     elif b[0]=='ChangeAll':
#         a=a.replace(b[1],b[2])
#
#
# print(f"The decrypted message is: {''.join(a)}")