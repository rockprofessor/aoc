data=[i.strip() for i in open('day3.in')]

w1 = [i for i in data[0].split(',')]
w2 = [i for i in data[1].split(',')]

cross = []

go = {'R': (1,0),
            'L': (-1,0),
            'U': (0,1),
            'D': (0,-1)}

path1 = [(0,0)]
for r in w1:
    dir = r[0]
    step = int(r[1:])
    path1.append((path1[-1][0]+go[dir][0] * step,path1[-1][1]+go[dir][1] * step))

path2 = [(0,0)]
for r in w2:
    dir = r[0]
    step = int(r[1:])
    path2.append((path2[-1][0]+go[dir][0] * step,path2[-1][1]+go[dir][1] * step))  
    q1 = (path2[-2][0],path2[-2][1])
    q2 = (path2[-1][0],path2[-1][1])
    for i in range(len(path1)-1):
        p1 = (path1[i][0],path1[i][1])
        p2 = (path1[i+1][0],path1[i+1][1])
        if q1[0] == q2[0]:
            if min(p1[0],p2[0]) < q1[0] < max(p1[0],p2[0]) and min(q1[1],q2[1]) < p1[1] < max(q1[1],q2[1]):
                point = (q1[0],p1[1])
                if point not in cross: cross.append(point)
        if q1[1] == q2[1]:
            if min(p1[1],p2[1]) < q1[1] < max(p1[1],p2[1]) and min(q1[0],q2[0]) < p1[0] < max(q1[0],q2[0]):
                point = (p1[0],q1[1])
                if point not in cross: cross.append(point)

dist = []
for i in cross:
    dist.append(abs(i[0])+abs(i[1]))
dist.sort()
print('Answer 1:',dist[0])

score = []
for c in cross:
    count=0
    pos = (0,0)
    for r in w1:
        if pos == c: break
        dir = r[0]
        step = int(r[1:])   
        for s in range(step):
            pos = (pos[0]+go[dir][0],pos[1]+go[dir][1])
            count +=1
            if pos == c: break
    pos = (0,0)
    for r in w2:
        if pos == c: break
        dir = r[0]
        step = int(r[1:])
        for s in range(step):
            pos = (pos[0]+go[dir][0],pos[1]+go[dir][1])
            count +=1
            if pos == c: break
    score.append(count)
print('Answer 2:',min(score))
