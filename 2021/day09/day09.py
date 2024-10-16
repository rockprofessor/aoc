import numpy as np

data = [i.strip() for i in open('test.in')]

map = []
for line in data:
    map.append([int(x) for x in list(line.strip())])

map = np.array(map)

R = len(map)     # rows
C = len(map[0])  # coloums
DR = [-1,0,1,0]  # directions to look
DC = [0,-1,0,1]  # directions to look

sum = 0
bas = {}

for r in range(R):
    for c in range(C):
        check = 1
        for d in range(4):
            rr = r + DR[d]
            cc = c + DC[d]
            if 0 <= rr < R and 0 <= cc < C and map[rr][cc] <= map[r][c]:
                check = 0
        if check == 1: 
            sum += map[r][c]+1
            bas[(r,c)] = [(r,c)]    #for part 2
print('Answer 1:',sum)

#part 2*******************************+

for low in bas:
    print('******************')
    print('pos lowpoint:',low)
    r=0
    for pos in bas[low]:
        r +=1
        print('runde:',r)
        print('check',pos)
        print()
        add = []
        r = pos[0]
        c = pos[1]
        for d in range(4):
            rr = r + DR[d]
            cc = c + DC[d]
            if 0 <= rr < R and 0 <= cc < C and map[rr][cc] < 9:
                if (rr,cc) not in bas[low[0],low[1]]: 
                    add.append((rr,cc))
        bas[low[0],low[1]] += add 

sum = []
for item in bas:
    sum.append(len(bas[item]))

sum.sort()
print('Answer 2:',sum[-1]*sum[-2]*sum[-3])
