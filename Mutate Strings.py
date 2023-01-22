a=input()
b=input()

l=len(a)
n=''

for i in range(l):
    if a[i]==b[i]: n+=b[i:i+1]

    else:
        n+=b[i:i+1]
        print(n+a[i+1:])