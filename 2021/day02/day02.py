data = [i.strip() for i in open('day2.in')]
x=0
y=0

for i in data:
    a,b=i.split(' ')
    if a=='forward':
        x+=int(b)
    if a=='up':
        y-=int(b)
    if a=='down':
        y+=int(b)
print('Answer 1:',x*y)

x=0
y=0
aim=0
for i in data:
    a,b=i.split(' ')
    if a=='forward':
        x+=int(b)
        y+=aim*int(b)
    if a=='up':
        aim-=int(b)
    if a=='down':
        aim+=int(b)
print('Answer 2:',x*y)
