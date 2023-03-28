import re

n=int(input())
r=r'@(#+)(?P<code>[A-Z][a-zA-Z0-9]{4,}[A-Z])@\1'

for i in range(n):
    a=input()
    t=re.finditer(r,a)
    print(t)
    for i in t:
        print(i)