import numpy as np
data = [i.strip() for i in open('test.in')]

coord = []
def mandist(r):
    return abs(r[0]-r[2]) + abs(r[1]-r[3])

for x in data:
    a,b = x.split(': closest beacon is at x=')
    a = a[12:]
    s1,s2 = a.split(', y=')
    b1,b2 = b.split(', y=')
    s1,s2,b1,b2 = [int(x) for x in [s1,s2,b1,b2]]
    coord.append([s1,s2,b1,b2])

for h in coord:
    h.append(mandist(h))
    
coord = np.array(coord)
print(coord)
print()
m = coord.max(axis=0)
n = coord.min(axis=0)
xmax = max(m[0],m[2])
ymax = max(m[1],m[3])
xmin = min(n[0],n[2])
ymin = min(n[1],n[3])

row = 10
c = 0
result = ''
for k in range(xmin,xmax+1):
    clear = 1
    for j in coord:
        if mandist([k,row,j[0],j[1]]) < j[4]:
            clear = 0
    if clear == 1 : result += '.'
    else: result += '#'
print(result)
