data = [i.strip() for i in open('10.in')]

def look(p):
    togo = []
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for n in range(4):
        test = (p[0] + d[n][0], p[1] + d[n][1])
        if test in map:
            if map[test] == map[p] + 1: togo.append(test)
    return togo

map = {}
starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        map[(i, j)] = int(data[i][j])
        if data[i][j] == '0': starts.append((i, j))

ans1 = 0
for start in starts:
    current = [start]
    for step in range(9):
        new = set() 
        for c in current:
            for n in look(c):
                new.add(n)
        current = []
        for n in new: current.append(n)
    ans1 += 1
print('Answer 1:', ans1)

trails = []
for start in starts: trails.append([start])

for step in range(9):
    newtrails = []
    while trails:
        go = trails.pop(0)
        new = look(go[-1])
        for n in new: newtrails.append(go + [n])
    for newt in newtrails: trails.append(newt)
print('Answer 2:', len(trails))


