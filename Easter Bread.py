a=float(input())
f=float(input())
e=0.75*f
m=1.25*f*0.25
count=0
colo=0
k=0

while a>=(f+e+m):
    a-=(f+e+m)
    count += 1
    colo += 3
    k-=1
    if count%3==0: colo-=(count-2)

print(f"You made {count} loaves of Easter bread! Now you have {colo} eggs and {a:.2f}BGN left.")