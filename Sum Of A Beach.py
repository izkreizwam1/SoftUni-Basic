a=input()
# a='GolDeNSanDyWateRyBeaChSuNN'
a=a.lower()
k=["sand", "water", "fish", "sun"]

c=sum(a.count(i) for i in k)
print(c)