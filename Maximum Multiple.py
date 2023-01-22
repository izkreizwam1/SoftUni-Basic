a= int(input())
b=int(input())

for i in range(b,-1,-1):
    if i%a==0 :
        print(i)
        exit()