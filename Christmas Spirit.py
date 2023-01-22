x= int(input())
a=int(input())

s=0
p=0




for i in range(1,a+1):
    if i%11==0:
        x+=2
    if i%2==0:
        s+=5
        p+=2*x
    if i%3==0:
        s+=13
        p+=8*x
    if i%5==0:
        s+=17
        p+=15*x
    if i%15==0:
        s+=30
    if i%10==0:
        s-=20
        p+=23
    if i % 10 == 0 and i==a:
        s-=30
    # if i%11==0:
    #     x+=2

print(f"Total cost: {p}\nTotal spirit: {s}")