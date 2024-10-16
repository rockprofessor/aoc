with open("day8.in") as f:
        data = f.read().split()
n=len(data)
m=len(data[0])

vis=0
vis=2*n+2*m-4 #trees outline
view=0
map=[]
t=0
for i in range(m):
    treecol=''
    for j in range(n):
        treecol+=(data[j][i])
    map.append(treecol)

for j in range(1,m-1):
    for i in range(1,n-1):
        a,b=int(max(data[i][:j])),int(max(data[i][j+1:]))
        c,d=int(max(map[j][:i])),int(max(map[j][i+1:]))
        t=int(data[i][j])
        if t>a or t>b or t>c or t>d:
            vis+=1


def look(p):
    vl=0 
    for r in range(p[1]-1,-1,-1):       #left
        if int(data[p[0]][r])<int(data[p[0]][p[1]]):
            vl+=1
        elif int(data[p[0]][r])==int(data[p[0]][p[1]]):
            vl+=1
            break
        else:
            vl+=1
            break
    vr=0
    for r in range(p[1]+1,m):          #right
        if int(data[p[0]][r])<int(data[p[0]][p[1]]):
            vr+=1
        elif int(data[p[0]][r])==int(data[p[0]][p[1]]):
            vr+=1
            break
        else:
            vr+=1
            break
    vu=0
    for r in range(p[0]-1,-1,-1):    #up
        if int(data[r][p[1]])<int(data[p[0]][p[1]]):
            vu+=1
        elif int(data[r][p[1]])==int(data[p[0]][p[1]]):
            vu+=1
            break
        else:
            vu+=1
            break
    vd=0
    for r in range(p[0]+1,n):       #down
        if int(data[r][p[1]])<int(data[p[0]][p[1]]):
            vd+=1
        elif int(data[r][p[1]])==int(data[p[0]][p[1]]):
            vd+=1
            break
        else:
            vd+=1
            break  
    return(vl*vr*vu*vd)

viewlist=[]
for i in range(1,n-1):
    for j in range(1,m-1):
        viewlist.append((look([i,j])))
print('Answer 1:',vis)
print('Answer 2:',max(viewlist))
