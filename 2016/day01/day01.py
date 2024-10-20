import copy
data = open('day1.in').read().split(', ')

dir = [(0,1),(1,0),(0,-1),(-1,0)]
pos = [(0,0)]
d = 0
ans = (0,0)

for x in data:
    if x[0] == 'R': d = (d+1) % 4
    else: d = (d+3) % 4
    steps = int(x[1:])
    for s in range(steps):
        pos.append((pos[-1][0] + dir[d][0], pos[-1][1] + dir[d][1]))

for g in pos:
    if pos.count(g) == 2: 
        found = g
        break

print('Answer 1:', sum(pos[-1]))
print('Answer 2:', sum(found))



