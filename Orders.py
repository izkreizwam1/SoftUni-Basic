a= int(input())
k=0
for i in range(a):
    p=float(input())
    d=int(input())
    c=int(input())
    if 0.01<=p<=100 and 1<=d<=31 and 1<=c<=2000:
        print(f'The price for the coffee is: ${p*d*c:.2f}')
        k+=p*c*d
    else: pass

print(f"Total: ${k:.2f}")