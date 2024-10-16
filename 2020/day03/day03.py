data=[i.strip() for i in open('day3.in')]
map=set()

for j in range(0,len(data)):
    for i in range(0,len(data[0])):
        if data[j][i]=='#': map.add((i,j))
    
def walk(x,y):
    count=0
    pos=(0,0)
    while pos[1]<max([i[1] for i in map]):
        pos=((pos[0]+x)%len(data[0]),pos[1]+y)
        if pos in map: count+=1
    return(count)

print('Answer 1:',walk(3,1))
#--------------------------------
prod=1
prod*=walk(1,1)
prod*=walk(3,1)
prod*=walk(5,1)
prod*=walk(7,1)
prod*=walk(1,2)
print('Answer 2:',prod)
