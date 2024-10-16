import numpy as np
data = [i.strip() for i in open('day10.in')]

pos = []
vel = []

def printmap(m):
    for z in m:
        r = ''
        for i in z:
            if i == 1: r +='#'
            else: r +='.'
        print(r)
    print()
        


for line in data:
    line = line[10:-1]
    p,v = line.split('> velocity=<')
    p = p.strip().split(', ')
    v = v.strip().split(', ')
    p = [int(p[0]),int(p[1])]
    v = [int(v[0]),int(v[1])]
    pos.append(p)
    vel.append(v)


for r in range(10102):
    xmin = min([x for x,y in pos])
    xmax = max([x for x,y in pos])
    ymin = min([y for x,y in pos])
    ymax = max([y for x,y in pos])

    for i in pos:
        i[0] -= xmin
        i[1] -= ymin
        
    map = np.zeros((ymax-ymin+1,xmax-xmin+1),dtype = int)
    
    for i in pos: map[i[1],i[0]] = 1
    
    for z in range(len(pos)):
        pos[z][0] += vel[z][0]
        pos[z][1] += vel[z][1]

print()
print('Seconds:',r)
printmap(map)
