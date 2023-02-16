# # 5.	Multiplication Sign
# l=[int(input()),int(input()),int(input())]
# x=True
# for i in l:
#     if bool(i)==False:
#         print('zero')
#         exit()
#     if '-' in str(i): x= not x
# if x : print('positive')
# else:print('negative')

# # 4.	Tribonacci Sequence
# a=int(input())-2
# l=[1]
# while a>=0:
#     l.append(sum(i for i in l[-3::1]))
#     a-=1
# print(' '.join([str(i) for i in l]))

# # 3.	Longer Line
# import math
# def Center_Point(x,y):
#     sq=lambda x,y : (x[0]**2+x[1]**2)-(y[0]**2+y[1]**2)
#     if sq(x,y)<=0: print(tuple(math.floor(i) for i in x),tuple(math.floor(i) for i in y),sep='')
#     else: print(tuple(math.floor(i) for i in y),tuple(math.floor(i) for i in x), sep = '')
#
# l1=[[float(input()), float(input())],[float(input()), float(input())]]
# l2=[[float(input()), float(input())],[float(input()), float(input())]]
# l1_m=[i-j for i,j in zip(l1[0],l1[1])]
# l2_m=[i-j for i,j in zip(l2[0],l2[1])]
# long_l = lambda x, y: (x[0] ** 2 + x[1] ** 2) - (y[0] ** 2 + y[1] ** 2)
# if long_l(l1_m,l2_m)>=0 : Center_Point(l1[0],l1[1])
# else: Center_Point(l2[0],l2[1])


# # Center Point
# import math
# x=[float(input()),float(input())]
# y=[float(input()),float(input())]
# sq=lambda x,y : (x[0]**2+x[1]**2)-(y[0]**2+y[1]**2)
# if sq(x,y)<=0: print(tuple(math.floor(i) for i in x))
# else: print(tuple(math.floor(i) for i in y))

# # 01. Data Types
# a= input()
# def read(a):
#     if a=='int': return print(int(input())*2)
#     elif a=='real': return print(f'{float(input())*1.5:.2f}')
#     elif a=='string': return print(f'${input()}$')
# b=read(a)

# # 12. * Factorial Division
# a=int(input())
# b=int(input())
# fact=lambda x : 1 if x<=1 else x*fact(x-1)
# print(f'{fact(a)/fact(b):.2f}')

# # 11. * Loading Bar
# a=int(int(input())/10)
# l=a*['%']+(10-a)*['.']
#
# if a==10:
#     print('100% Complete!')
#     print(f'[{"".join(l)}]')
# else:
#     print(f'{a*10}% [{"".join(l)}]')
#     print('Still loading...')

# # 10. Perfect Number
# a= input()
# def find_sum(number):
#     sum=0
#     for i in range(1,int(number)):
#         if int(number)%int(i)==0: sum+=int(i)
#     return sum
# if int(a)==find_sum(a): print("We have a perfect number!" )
# else: print("It's not so perfect." )


# # 9. Password Validator
# a=input()
#
# def check_pass(password):
#     digits=['0','1','2','3','4','5','6','7','8','9']
#     p_length=True
#     p_chars=True
#     p_digit=True
#     digit_count=0
#     if 10<len(password) or len(password)< 6: p_length = False
#     for i in a:
#         i=ord(i)
#         if i not in range(48,58) and i not in range(65,91) and i not in range(97,123):
#             p_chars=False
#             continue
#     for i in a:
#         if i in digits: digit_count+=1
#     if digit_count<2: p_digit=False
#     return [p_length,p_chars,p_digit]
#
# l=check_pass(a)
# if l[0]==False: print("Password must be between 6 and 10 characters")
# if l[1]==False: print("Password must consist only of letters and digits")
# if l[2]==False: print("Password must have at least 2 digits")
# if sum(l)==3 : print("Password is valid")


# # 8. Palindrome Integers
# a= input().split(', ')
# b=[bool(x==x[::-1]) for x in a]
# print(*b,sep='\n')

# a=sorted([int(x) for x in input().split(' ')])
# print(f"The minimum number is {a[0]}")
# print(f"The maximum number is {a[-1]}")
# print(f"The sum number is: {sum(a)}")

# a= input().split(' ')
# b=sorted(list(int(x) for x in a))
# print(b)

# a= input().split(' ')
# b= filter(lambda x: int(x)%2==0,a)
# print(list(int(x) for x in b))

# a= input()
# o=[[int(x) for x in a if int(x)%2==0],[int(x) for x in a if int(x)%2==1]]
# print(f"Odd sum = {sum(o[1])}, Even sum = {sum(o[0])}")

# a,b=ord(input()),ord(input())
# l=[(lambda x: chr(x))(x) for x in range(a+1,b)]
# print(' '.join(l))

# a=int(input())
# b=int(input())
# c=int(input())
# def sum_numbers(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def add_and_subtract(a,b,c):
#     return subtract(sum_numbers(a,b),c)
#
# print(add_and_subtract(a,b,c))

# a=[int(input()),int(input()),int(input())]
# print((sorted(a))[0])

# a=input().split(' ')
# a=list(map(round,list(map(float,a))))
# print(a)

# a=int(input())*int(input())
# print(a)

# a=input()
# b=int(input())
# d={"coffee":1.5, "coke":1.4, "water":1, "snacks":2}
# print(f'{(lambda a,b :d[a]*b)(a,b):.2f}')

# a=input()
# b=int(input())
# print((lambda a,b: a*b)(a,b))

# a=[input(),int(input()), int(input())]
# def solve(a):
#     r=None
#     if a[0]=='multiply': r=a[1]*a[2]
#     elif a[0]=='divide': r=a[1]/a[2]
#     elif a[0]=='add' : r=a[1]+a[2]
#     elif a[0]=='subtract' : r=a[1]-a[2]
#     return int(r)
# print(solve(a))

# a=float(input())
# d={2<=a<=2.99:'Fail',3<=a<=3.49:'Poor',3.50<=a<=4.49:'Good', 4.50<=a<=5.49:'Very Good', 5.49<=a<=6:'Excellent'}
# print(d[True])

# a= input().split(' ')
# print([abs(float(x)) for x in  a])