a= int(input())
l=[0]

for i in range(a):
    w=int(input())
    t=int(input())
    q=int(input())
    if l[-1]<(w/t)**q : l=[w,t,(w/t)**q,q]

print(f"{l[0]} : {l[1]} = {l[2]:.0f} ({l[3]})")
