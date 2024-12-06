data = [i.strip() for i in open('t.in')]

look =       [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions = [ '>',    'v',    '<',     '^'   ]
r = len(data)
obs = []

for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char in  directions:
            pos = (l, c)
            lo = directions.index(char)
        if char == '#':
            obs.append((l, c))

obsrow ={i:[] for i in range(r)}
obscol ={i:[] for i in range(r)}

for o in obs:
    obsrow[o[0]].append(o[1])
    obscol[o[1]].append(o[0])

for i in range(r):
    obsrow[i].sort()
    obscol[i].sort()
t = True
while True:
    print(pos, lo)
    if lo == 0:     #right
        for i in range(pos[1], r):
            if i in obsrow[pos[0]]:
                pos = (pos[0], i - 1)
                lo = (lo + 1) % 4
                break
            if i == r - 1:
                t = False
    elif lo == 1:   #down
        for i in range(pos[0], r):
            if i in obscol[pos[1]]:
                pos = (i - 1, pos[1])
                lo = (lo + 1) % 4
                break
            if i == r - 1:
                t = False
    elif lo == 2:   #left
        for i in range(pos[1], -1, -1):
            if i in obsrow[pos[0]]:
                pos = (pos[0], i + 1)
                lo = (lo + 1) % 4
                break
            if i == 0:
                t = False
    elif lo == 3:   #up
        for i in range(pos[0], -1, -1):
            if i in obscol[pos[1]]:
                pos = (i + 1, pos[1])
                lo = (lo + 1) % 4
                break
            if i == 0:
                t = False
    if not t:
        break
