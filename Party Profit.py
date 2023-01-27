a= int(input())
b= int(input())
t=0

for i in range(1,b+1):
    if i % 10 == 0: a -= 2
    if i%15==0:
        a+=5
        t-=2*a

    if i%5==0: t+=20*a
    if i % 3 == 0: t -= a * 3
    t += (50 - a * 2)


print(f"{a} companions received {int(t/a)} coins each.")