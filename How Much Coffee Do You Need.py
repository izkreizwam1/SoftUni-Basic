a=input()
l=['coding','dog','cat','movie']
L=[x.upper() for x in l]
k=0

while a!='END':
    if a in l: k+=1
    elif a in L: k+=2
    a=input()

if k>5 : print("You need extra sleep")
else: print(k)