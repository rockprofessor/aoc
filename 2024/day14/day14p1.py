data = [i.strip() for i in open('14.in')]
#real input
xmax = 101
ymax = 103

#test input
#xmax = 11
#ymax = 7


rob = []
for line in data:
    p, v = line.split()
    px, py = p[2:].split(',')
    px = int(px)
    py = int(py)
    vx, vy = v[2:].split(',')
    vx = int(vx)
    vy = int(vy)
    rob.append([px, py, vx, vy])

for r in range(len(rob)):
    for t in range(100):
        #print(rob[r])
        if rob[r][0] + rob[r][2] >= xmax:
            rob[r][0] = rob[r][0] + rob[r][2] - xmax
        elif rob[r][0] + rob[r][2] < 0:
            rob[r][0] = rob[r][0] + rob[r][2] + xmax
        else:
            rob[r][0] += rob[r][2]

        if rob[r][1] + rob[r][3] >= ymax:
            rob[r][1] = rob[r][1] + rob[r][3] - ymax
        elif rob[r][1] + rob[r][3] < 0:
            rob[r][1] = rob[r][1] + rob[r][3] + ymax 
        else:
            rob[r][1] += rob[r][3]
    #print()

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for r in rob:
    if r[0] < (xmax-1)/2:
        if r[1] < (ymax-1)/2:
            q1 += 1
        elif r[1] > (ymax-1)/2:
            q2 += 1
    elif r[0] > (xmax-1)/2:
        if r[1] < (ymax-1)/2:
            q3 += 1
        elif r[1] > (ymax-1)/2:
            q4 += 1
print(q1 * q2 * q3 *q4)
