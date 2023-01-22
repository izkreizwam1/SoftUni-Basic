a=input()
l=[]
for i in range(len(a)):
    if ord('A')<=ord(a[i])<=ord('Z'):
        l.append(i)

print(l)