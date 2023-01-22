a= float(input())

k=''
if abs(a)>1000000: k='large'
elif 0<abs(a)<1: k='small'
d={a==0:'zero',0>a:'negative',0<a:'positive'}

print(k,d[True])