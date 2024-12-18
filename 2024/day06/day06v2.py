data = [i.strip() for i in open('6.in')]
grid = {}

for r in range(len(data)):
    for c in range(len(data[0])):
        grid[(r,c)] = data[r][c]
        if data[r][c] not in '#.': start = (r,c)

if grid[start] == '>': dr, dc = 0, 1
if grid[start] == 'v': dr, dc = 1, 0
if grid[start] == '<': dr, dc = 0, -1
if grid[start] == '^': dr, dc = -1, 0

visited = [start]
look = [(dr,dc)]

p = start
while True:
    new = (p[0] + dr, p[1] + dc)
    if new not in grid: break
    if grid[new] == '#': dr, dc = dc, -dr
    else:
        p = new
        visited.append(p)
        look.append((dr, dc))
print('Answer 1:', len(set(visited)))

lc = 0
for i in range(1, len(visited)):
    pos = visited[i - 1]
    o = visited[i]
    (dr, dc) = look[i - 1]
    vis = [(pos, dr, dc)]

    while (pos[0] + dr, pos[1] + dc) in grid:
        if grid[(pos[0] + dr, pos[1] + dc)] == '#' or (pos[0] + dr, pos[1] + dc) == o:
            dr, dc = dc, -dr
        else:
            pos = (pos[0] + dr, pos[1] + dc)
        if (pos, dr, dc) in vis:
            lc += 1
            break
        vis.append((pos, dr, dc))
print('Answer 2:', lc)
