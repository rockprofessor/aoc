with open("day9.in", "r") as angabe:
        data = angabe.read().split('\n')

hx=0
hy=0
tx=0
ty=0
way=[]

for x in data:
    dir,step=x.split(' ')
    step=int(step)
    for i in range(0,step):
        if dir=='R':   hx+=1
        elif dir=='L': hx-=1
        elif dir=='U': hy+=1
        elif dir=='D': hy-=1
        if pow((hy-ty),2)+pow((hx-tx),2)>2:
            if hx>tx: tx+=1
            elif hx<tx: tx-=1
            if hy>ty: ty+=1
            elif hy<ty: ty-=1
        way.append(str(tx)+' '+str(ty))
nummber_tail_pos = len(list(set(way)))
print('Answer 1:',nummber_tail_pos)

#-----------------------------------------------

v = set([(0, 0)])

R = [[0, 0] for i in range(10)]
A = [0, 0]
B = [0, 0]

def prmap():
    map=[]
    for t in range(0,10): print(R[t])
    for j in range(15,-6,-1):
        line=''
        for i in range(-11,17):
            d='.'
            for z in range(9,-1,-1):
                if R[z]==[i,j]: 
                    if z==0: d='H'
                    elif z==9: d='T'
                    else: d=str(z)
            line+=d
        map.append(line)
    for w in map:
        print(w)
    print()

for line in open("day9.in"):
    x, y = line.split(' ')
    y = int(y)
    dx = 0
    dy = 0
    for i in range(y):
        if x == 'R': dx = 1
        elif x == 'L': dx = -1
        elif x == 'U': dy = 1
        elif x == 'D': dy = -1

        #prmap()

        R[0][0] += dx
        R[0][1] += dy

        for j in range(9):
            A = R[j]
            B = R[j + 1]
            diffX = A[0] - B[0]
            diffY = A[1] - B[1]

            if abs(diffX) > 1 or abs(diffY) > 1:
                if diffX == 0: B[1] += diffY // 2
                elif diffY == 0: B[0] += diffX // 2
                else:
                    if diffX > 0: B[0] += 1
                    else: B[0] -= 1
                    if diffY > 0: B[1] += 1
                    else: B[1] -= 1
        v.add(tuple(B))
print('Answer 2:',len(v))
