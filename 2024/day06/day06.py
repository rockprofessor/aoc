data = [i.strip() for i in open('t.in')]
look = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions = ['>', 'v', '<', '^']
r = len(data)

for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char in  directions:
            pos = (l, c)
            visited = [pos]     #store visited coordinates
            lo = directions.index(char)
            go =[lo]

while 0 <= pos[0]+look[lo][0] < r and 0 <= pos[1]+look[lo][1] < r:
    if data[pos[0] + look[lo][0]][pos[1] + look[lo][1]] == '#':
        lo = (lo + 1) % 4   #turn 90° clockwise
    else:
        pos = (pos[0] + look[lo][0], pos[1] + look[lo][1])
        visited.append(pos)
        go.append(lo)
print('Answer 1:', len(set(visited)))

lc = 0
for i in range(1, len(visited)):
    o = visited[i]
    pos = visited[i -1]
    n = go[i - 1]
    vis = [(pos, n)]
    dr = look[n][0] 
    dc = look[n][1]

    while 0 <= pos[0] + dr < r and 0 <= pos[1] + dc < r:
        dr = look[n][0] 
        dc = look[n][1]
        if data[pos[0] + dr][pos[1] + dc] == '#' or (pos[0] + dr,pos[1] + dc) == o:
            n = (n + 1)%4
        else:
            pos = (pos[0] + dr, pos[1] + dc)
        if (pos, n) in vis:
            lc += 1
            break
        vis.append((pos, n))
print('Answer 2:', lc)
