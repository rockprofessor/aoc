data = [i.strip() for i in open('6.in')]
look = [(0, 1), (1, 0), (0, -1), (-1, 0)]
directions = ['>', 'v', '<', '^']
r = len(data)

for l, line in enumerate(data):
    for c, char in enumerate(line):
        if char in  directions:
            pos = (l, c)
            visited = [pos]     #store visited coordinates
            lo = directions.index(char)
            sdir = lo   #first look direction for part 2

while 0 <= pos[0]+look[lo][0] < r and 0 <= pos[1]+look[lo][1] < r:
    if data[pos[0] + look[lo][0]][pos[1] + look[lo][1]] == '#':
        lo = (lo + 1) % 4   #turn 90° clockwise
    else:
        pos = (pos[0] + look[lo][0], pos[1] + look[lo][1])
        if pos not in visited:
            visited.append(pos)

print('Answer 1:', len(visited))

letsgo = visited.pop(0)
loopcount = 0

for o in visited:
    pos = letsgo
    lo = sdir
    vis = [(pos, lo)]
    while 0 <= pos[0]+look[lo][0] < r and 0 <= pos[1]+look[lo][1] < r:
        if data[pos[0]+look[lo][0]][pos[1]+look[lo][1]] == '#' or (pos[0]+look[lo][0],pos[1]+look[lo][1]) == o:
            lo = (lo + 1)%4
            if (pos, lo) in vis:
                loopcount += 1
                break
            vis.append((pos, lo))

        else:
            pos = (pos[0] + look[lo][0], pos[1] + look[lo][1])
            if (pos, lo) in vis:
                loopcount += 1
                break

            vis.append((pos, lo))
print('Answer 2:', loopcount)

     

