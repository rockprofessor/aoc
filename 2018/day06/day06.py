data = [i.strip() for i in open('day6.in')]

coord = []
for line in data:
    x,y = line.split(', ')
    coord.append((int(x),int(y)))

xmax = max([x for x,y in coord])
ymax = max([y for x,y in coord])

def md(P,Q):
    return abs(P[0]-Q[0]) + abs(P[1]-Q[1])

mdis = {G:[] for G in coord}

for cx in range(xmax+1):
    for cy in range(ymax+1):
        C = (cx,cy)
        mini = 2*xmax  
        two = False
        for P in coord:
            if md(P,C) == mini: two = True
            if md(P,C) < mini:
                two = False
                mini = md(P,C)
                R = P
        if two == False: mdis[R].append(C)

finite = []

for l in mdis:
    if max([x for x,y in mdis[l]]) < xmax and min([x for x,y in mdis[l]]) > 0 and max([y for x,y in mdis[l]]) < ymax and min([y for x,y in mdis[l]]) > 0:
        finite.append(len(mdis[l]))
print('Answer 1:',max(finite))

#part 2****************
count = 0
for cx in range(xmax+1):
    for cy in range(ymax+1):
        C = (cx,cy)
        sum = 0
        for P in coord:
            sum += md(P,C)
        if sum < 10000:
            count += 1

print('Answer 2:',count)
