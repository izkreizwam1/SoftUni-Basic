a= int(input())
t=0
d={'h':float(input()),'s':float(input()),'d':float(input()),'a':float(input()),}

for i in range(1,a+1):
    if i%2==0: t+=d['h']
    if i%3==0: t+=d['s']
    if i%6==0: t+=d['d']
    if i%12==0: t+=d['a']

print(f"Gladiator expenses: {t:.2f} aureus")