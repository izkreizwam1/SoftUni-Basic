a=int(input())
k=255

for i in range(a):
    b=int(input())
    if k-b<0:
        print('Insufficient capacity!')
    else:
        k-=b

print(255-k)