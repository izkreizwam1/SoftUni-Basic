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