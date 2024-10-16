import numpy as np
data = [i.strip() for i in open('test.in')]

inp = []
for line in data:
    inp.append([int(i) for i in line.split(',')])

cubes = len(inp)
z =np.array(inp)
max = np.max(z, axis = 0)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

touch = 0
for r in inp:
    for d in range(6):
        nx = r[0]+dx[d]
        ny = r[1]+dy[d]
        nz = r[2]+dz[d]
        if 0 <= nx <= max[0] and 0 <= ny <= max[1] and 0 <= nz <= max[2]:
            if [nx, ny, nz] in inp: 
                touch +=1
 
print('Answer 1:',cubes*6-touch)

voids = 0
for x in range(1,max[0]):
    for y in range(1,max[1]):
        for z in range(1,max[2]):
            count = 0
            for d in range(6):
                if [x+dx[d],y+dy[d],z+dz[d]] in inp and [x,y,z] not in inp: count += 1
            if count == 6: voids += 1
print(cubes*6-touch-voids*6)


#  1-dim test
inp = [4,5,7,8]
voidcan = [0,1,2,3,6,9,10,11]    #ränder entfernen

max = 11
voidmap = []
while len(voidcan) > 0:
    void = []
    n = voidcan[0]
    print(n)
    void.append(n)
    isvoid = True
    for i in void:
        if 0 < i-1:
            if i-1 in voidcan: 
                if i-1 not in void: void.append(i-1)
                voidcan.remove(i-1)
        else: isvoid = False
        if i+1 <= max:
            if i+1 in voidcan: 
                if i+1 not in void: void.append(i+1)
                voidcan.remove(i+1)
        else: isvoid = False   
    if isvoid: 
        voidmap.append(sorted(void))
    else:
        for i in void: 
            if i in voidcan: 
                voidcan.remove(i)
print(voidmap)
print(voidcan)
