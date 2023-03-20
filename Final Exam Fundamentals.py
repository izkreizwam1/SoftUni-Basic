# The Pianist
def add(p,c,k,d):
    if p in d:
        print(f"{p} is already in the collection!")
        return d
    else:
        d[p]=[c,k]
        print(f"{p} by {c} in {k} added to the collection!")
        return d



n= int(input())
d={}
for i in range(n):
    a= input().split('|')
    d[a[0]]=[a[1],a[2]]
while True:
    b=input()
    if b=='Stop': break
    b=b.split('|')
    if b[0]=='Add':
        d=add(b[1],b[2],b[3],d)
    elif b[0]=='Remove':
        pass
    elif b[0]=='ChangeKey':
        pass





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