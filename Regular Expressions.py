import re

# # 5.	HTML Parser
# a= input()
# l=[]
# l1=[]
# # r=r'[>|(?<=\\n)|(?<=\\t)]([\w\s\-\.]*)[<|(?=\\n)|(?<=\\t)]'
# r=r'[>|(?<=\\n)]([\w\s\-\.]*)[<|(?=\\n)]'
# r_t=r'<title>.*<\/title>'
# r_b=r'<body>.*<\/body>'
# t=re.findall(r_t,a)
# b=re.findall(r_b,a)
# b[0]=b[0].replace('\t', '   ')
# m_t= re.findall(r,t[0])
# m_b=re.findall(r,b[0])
# for i in m_t:
#     if i :
#         l.append(i)
# for i in m_b:
#     if i:
#         l1.append(i)
# print(f"Title: {''.join(l)}")
# print(f"Content: {''.join(l1)}")


# # 4.	Nether Realms
# a=input().split(',')
# a=[i.strip() for i in a]
# list={}
# mul=[]
# r_h=r'[^0-9\+\-\*\/\.]'
# r_d=r'-?[0-9]+\.?[0-9]*'
# # pattern_damage = r"([-+]?\d+\.?\d+?)"
# for i in sorted(a):
#     if ' ' in i: continue
#     h=sum([ord(k) for k in re.findall(r_h,i)])
#     d=sum([float(k) for k in re.findall(r_d,i)])
#     for j in i:
#         if j=='*': d*=2
#         elif j=='/': d/=2
#     print(f"{i} - {h} health, {d:.2f} damage ")

# 3.	Star Enigma
# n= int(input())
# att=[]
# des=[]
# for i in range(n):
#     a=input()
#     r_code=r'(?i)[star]'
#     code=len(re.findall(r_code,a))
#     b=''
#     for j in range(len(a)):
#         b+=chr(ord(a[j])-code)
#     r=r'@([A-Z][a-z]+)[^\@\-\!\>]*:([0-9]+)[^\@\-\!\>]*!([A|D])![^\@\-\!\>]*->([0-9]+)'
#     matches=re.findall(r,b)
#     if matches:
#         if matches[0][2]=='A': att.append(matches[0][0])
#         elif matches[0][2]=='D': des.append(matches[0][0])
# att=sorted(att)
# # print(att)
# des=sorted(des)
# # print(des)
# print(f"Attacked planets: {len(att)}")
# for i in range(len(att)):
#     print(f"-> {att[i]}")
# print(f"Destroyed planets: {len(des)}")
# for i in range(len(des)):
#     print(f"-> {des[i]}")


# t=0
# while True:
#     a = input()
#     if a=='end of shift': break
#     r=r'%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|([0-9]+)\|[^\|\$\%\.]*?([0-9]+.?[0-9]+?)\$'
#     matches=re.findall(r,a)
#     if matches:
#         s=int(matches[0][2])*float(matches[0][3])
#         t+=s
#         print(f'{matches[0][0]}: {matches[0][1]} - {s:.2f}')
# print(f"Total income: {t:.2f}")

# # Race
# r_l=r'[A-Za-z]'
# r_d=r'[0-9]'
# l=input().split(', ')
# d=[[i,0] for i in l]
# while True:
#     a=input()
#     if a=='end of race': break
#     m_l=re.findall(r_l,a)
#     m_d=re.findall(r_d,a)
#     m_d= [int(i) for i in m_d]
#     name=''.join(m_l)
#     score=sum(m_d)
#     for i in d:
#         if name==i[0]:
#             i[1]+=score
# d.sort(key=lambda x: -x[1])
# print(f"1st place: {d[0][0]}\n2nd place: {d[1][0]}\n3rd place: {d[2][0]}")

# # Extract the Links
# r=r'(www.[A-Za-z0-9\-]+(\.[a-z]+)+)'
# a=input()
# while a:
#     matches = re.findall(r, a)
#     if matches:
#         for i in matches:
#             print(i[0])
#     a = input()

# 5.	Furniture
# t=0
# l=[]
# while True:
#     a=input()
#     if a=='Purchase': break
#     r=r'>>([A-Za-z]+)<<([0-9]+.?[0-9]*)!([0-9]+)'
#     maches=re.findall(r,a)
#     # print(maches)
#     if maches:
#         t+=float(maches[0][1])*int(maches[0][2])
#         l.append(maches[0][0])
#
# print('Bought furniture:')
# for i in l:
#     print(i)
# print(f"Total money spend: {t:.2f}")

# # 4.	Extract Email
# a=input()
# r=r'\s([0-9a-z]+[a-z0-9\.\_\-]*@[a-z\-]+(\.[a-z]+)+)\b'
# matches = re.findall(r, a)
# # print(matches)
# for i in matches:
#     # print('\n'.join(i[0]))
#     print(i[0])

# # Find Occurrences of Word in Sentence
# a=input()
# b=input()
# # r=rf'\b{b}\b'
# r=rf'(?i)\b{b}\b'
# matches = re.findall(r, a,re.IGNORECASE)
# print(len(matches))

# # Find Variable Names in Sentences
# a=input()
# r=r'\b_([0-9a-zA-Z]+)\b'
# matches = re.findall(r, a)
# print(','.join(matches))

# # Capture the Numbers
# r='\d+'
# a=input()
# while a:
#     matches = re.findall(r, a)
#     if matches:
#         print(' '.join(matches),end=' ')
#     a = input()

# # Match Numbers
# r='(^|(?<=\s))-?([0-9]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
# matches = re.finditer(r, a)
# for i in matches:
#     print(i.group(),end=' ')

## Match Dates
# r='\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b'
# matches = re.finditer(r, a)
# for i in matches:
#     print(f"Day: {i.group('day')}, Month: {i.group('month')}, Year: {i.group('year')}")

##Match Phone Number
# r='(\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4})\\b'
# matches = re.findall(r, a)
# print(", ".join(matches))

## Match Full Name
# names = input()
# regex = "\\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\\b"
# matches = re.findall(regex, names)
# print(" ".join(matches))
