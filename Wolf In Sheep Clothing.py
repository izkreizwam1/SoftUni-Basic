a=input()
l=a.split(', ')
for i in range(len(l)):
    if l[i]=='wolf':
        if l[i]==l[-1]: print("Please go away and stop eating my sheep")
        else: print(f"Oi! Sheep number {len(l)-1-i}! You are about to be eaten by a wolf!" )