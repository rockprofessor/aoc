data = [i.strip() for i in open('day3.in')]

map=[[]]
line=[]
for i in range(1000):
    map.append([])
    for j in range(1000):
        map[i].append(0)

for line in data:
    a,b=line.split(' @ ')
    nr=int(a[1:])
    c,d=b.split(': ')
    x,y=c.split(',')
    w,h=d.split('x')
    x=int(x)
    y=int(y)
    w=int(w)
    h=int(h)
    for j in range(y,y+h):
        for i in range(x,x+w):
            map[j][i]+=1
count=0
for line in map:
    for m in line:
        if m>1: count+=1
print('Answer 1:',count)

for line in data:
    a,b=line.split(' @ ')
    nr=int(a[1:])
    c,d=b.split(': ')
    x,y=c.split(',')
    w,h=d.split('x')
    x=int(x)
    y=int(y)
    w=int(w)
    h=int(h)
    free=1
    for j in range(y,y+h):
        for i in range(x,x+w):
            if map[j][i]>1: free=0
    if free==1: print('Answer 2:',nr)

