data = [i.strip() for i in open('t1.in')]
R = len(data)

walls = []
for r in range(R):
    for c in range(R):
        if data[r][c] == '#':
            walls.append((r, c))
        if data[r][c] == 'S':
            start = (r, c)
        if data[r][c] == 'E':
            end = (r, c)

def ac(a, b): return (a[0] + b[0], a[1] + b[1])

tiles = {}
d = (0, 1)

curr = [[[start], 0,    d]]
tiles[(start)] = [[start], 0,    d]
while curr:
    c = curr.pop()
    d = c[2]
    for t, togo in enumerate([d, (d[1], -d[0]), (-d[1],  d[0])]):
        new = ac(c[0][-1], togo) 
        if new in walls:
            continue
        if t == 0: cost = c[1] + 1
        else: cost = c[1] + 1001
        update = False
        if new in tiles:
            if tiles[new][1] == cost:
                tiles[new][0].append(c[0] + [new])

            if tiles[new][1] > cost:
                tiles[new] = [[c[0] + [new]], cost, togo]
                update = True
        else:
            tiles[new] = [[c[0] + [new]], cost, togo]
            update = True
        if update:
            curr.append([c[0] + [new], cost, togo])

z = 0
all = set(tiles[end][0][0])
for t in tiles[end][0][0]:
    if len(tiles[t][0]) > 1:
        for x in tiles[t][0]:
            for y in x:
                all.add(y)

print('Answer 1:', tiles[end][1])
print('Answer 2:', len(all))
