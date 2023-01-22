a= int(input())

d={88:'Hello',86:'How are you?'}
for i in range(a):
    b=int(input())
    if b>88: print('Bye.')
    elif b<88 and b!=86: print('GREAT!')
    else: print(d[b])