data=[i.strip() for i in open('day2.in')]

valid1=0
valid2=0
#1-3 a: abdgee
#a-b c: d
for line in data:
    words=line.split(' ')
    a,b=words[0].split('-')
    c=words[1][0]
    d=words[2]
    a=int(a)
    b=int(b)
    if a<=d.count(c)<=b: valid1+=1
    if (d[a-1]==c or d[b-1]==c) and not (d[a-1]==c and d[b-1]==c): valid2+=1
print('Answer 1:',valid1)
print('Answer 2:',valid2)
