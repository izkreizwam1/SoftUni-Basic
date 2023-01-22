a=int(input())
for i in range(a):
    b=int(input())
    if b%2==1:
        print(f"{b} is odd!" )
        break
else:
    print("All numbers are even.")