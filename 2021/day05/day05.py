data = [i.strip() for i in open('day5.in')]

s = []
e = []
xmax = 0
ymax = 0

def printmap(m):
    for h in m:
        line = ''
        for k in h:
            line += str(k)
        print(line)



for x in data:
    a,b = x.split(' -> ')
    x1,y1 = a.split(',')
    x2,y2 = b.split(',')
    x1,y1,x2,y2 = [int(x) for x in [x1,y1,x2,y2]]
    s.append([x1,y1])
    e.append([x2,y2])
    if x1 > xmax: xmax = x1
    if x2 > xmax: xmax = x2
    if y1 > ymax: ymax = y1
    if y2 > ymax: ymax = y2

#part 1
map=[]
for i in range(ymax+1):
    line=[]
    for j in range(xmax+1):
        line.append(0)
    map.append(line)

for k in range(len(s)):
    sx = s[k][0]
    sy = s[k][1]
    ex = e[k][0]
    ey = e[k][1]
    
    if sx == ex:  
        if s[k][1] < e[k][1]:
            for t in range(sy,ey+1):
                map[t][sx] += 1
        else:
            for t in range(ey,sy+1):
                map[t][sx] += 1
    if sy == ey:
        if sx<ex:
            for t in range(sx,ex+1):
                map[sy][t] += 1
        else:
            for t in range(ex,sx+1):
                map[sy][t] += 1

count=0
for i in map:
    for j in i:
        if j > 1:
            count += 1
print('Answer 1:',count)


#part2
map=[]
for i in range(ymax+1):
    line = []
    for j in range(xmax+1):
        line.append(0)
    map.append(line)


for k in range(len(s)):
    sx = s[k][0]
    sy = s[k][1]
    ex = e[k][0]
    ey = e[k][1]

    if sx == ex:  
        if s[k][1] < e[k][1]:
            for t in range(sy,ey+1):
                map[t][sx] += 1
        else:
            for t in range(ey,sy+1):
                map[t][sx] += 1
    elif sy == ey:
        if sx < ex:
            for t in range(sx,ex+1):
                map[sy][t] += 1
        else:
            for t in range(ex,sx+1):
                map[sy][t] += 1
    elif sx < ex and sy < ey:
        x = sx
        y = sy
        while x <= ex:
            map[y][x] += 1
            x += 1
            y += 1
    elif sx<ex and sy>ey:
        x = sx
        y = sy
        while x <= ex:
            map[y][x] += 1
            x += 1
            y -= 1

    elif sx > ex and sy > ey:
        x = sx
        y = sy
        while x >= ex:
            map[y][x] += 1
            x -= 1
            y -= 1
    elif sx > ex and sy < ey:
        x = sx
        y = sy
        while x >= ex:
            map[y][x] += 1
            x -= 1
            y += 1
#printmap(map)

count = 0
for i in map:
    for j in i:
        if j > 1:
            count += 1
print('Answer 2:',count)
