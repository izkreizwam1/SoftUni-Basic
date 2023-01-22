a=input()

def nn(a):
    m=''
    for j in range(len(a)):
        m+=2*a[j]
    return m

while a!='End':
    if a=='SoftUni':
        a=input()
    else:
        # m=nn(a)
        m=''
        for j in range(len(a)):
            m+=2*a[j]

        print(m)
        a=input()