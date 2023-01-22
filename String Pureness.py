a= int(input())
k=[',','.','_']
for i in range(a):
    p=input()
    if any(x in p for x in k): print(f"{p} is not pure!")
    else: print(f"{p} is pure.")