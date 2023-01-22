a= int(input())
b=input()

while b!='End':
    a-=int(b)
    if a<0 :
        print("You went in overdraft!" )
        break
    b=input()

else: print("You bought everything needed." )