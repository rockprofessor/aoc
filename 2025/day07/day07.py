# (col, row)
grid = {(x,y): c for y, row in enumerate(open('7.in')) for x, c in enumerate(row)}
for field in grid:
    if grid[field] == 'S':
        start = field

R = (max(grid.keys(), key=lambda x: x[1]))[1]
beam = [start]
c1 = 0
c2 = 0

i = 0
while i < R:
    newbeam = []
    while beam:
        pos = beam.pop(0)
        look = (pos[0], pos[1] + 1)
        if look in grid:
            if grid[look] == '^':
                newbeam.append((look[0] - 1, look[1]))
                newbeam.append((look[0] + 1, look[1]))
                c1 += 1
            else:
                newbeam.append(look)
        else:
            go = False

    for n in set(newbeam):
        beam.append(n)
    i += 1

print('Answer 1:', c1)


beam2 = {start: 1}
i = 0
while i < R:
    newbeam = {}
    while beam2:
        look, numb = beam2.popitem()
        look = (look[0], look[1] + 1)
        if look in grid:
            if grid[look] == '^':
                if (look[0] - 1, look[1]) in newbeam:
                    newbeam[(look[0] - 1, look[1])] += numb
                else:
                    newbeam[(look[0] - 1, look[1])] = numb
                if (look[0] + 1, look[1]) in newbeam:
                    newbeam[(look[0] + 1, look[1])] += numb
                else:
                    newbeam[(look[0] + 1, look[1])] = numb
            else:
                if look in newbeam:
                    newbeam[look] += numb
                else:
                    newbeam[look] = numb
    for n in newbeam:
        beam2[n] = newbeam[n]
    i += 1

c2 = 0
for k in newbeam:
    c2 += newbeam[k]

print('Answer 2:', c2)
