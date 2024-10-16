data=[i.strip() for i in open('day14.in')]

map={}
xmax=0
xmin=10000
ymax=0
ymin=10000
for line in data:
    word=line.split(' -> ')
    for i in range(0,len(word)-1):
        x1,y1=word[i].split(',')
        x2,y2=word[i+1].split(',')
        x1,x2,y1,y2=[int(x) for x in [x1,x2,y1,y2]]
        if x1<xmin: xmin=x1
        if x2<xmin: xmin=x2
        if x1>xmax: xmax=x1
        if x2>xmax: xmax=x2
        if y1<ymin: ymin=y1
        if y2<ymin: ymin=y2
        if y1>ymax: ymax=y1
        if y2>ymax: ymax=y2

        if x1==x2:
            for r in range(min(y1,y2),max(y1,y2)+1):
                    map[(x1,r)]='r'
        if y1==y2:
            for r in range(min(x1,x2),max(x1,x2)+1):
                map[(r,y1)]='r'


def printmap():
    for i in range(0,ymax+4):
        line=''
        for j in range(xmin-10,xmax+11):
            if (j,i) in map.keys() and map[(j,i)]=='r': line+='#'
            elif (j,i) in map.keys() and map[(j,i)]=='s': line+='o'
            else: line+='.'
        print(line)


printmap()

run=1
stonecounter=-1
while run==1:
    sand=[500,0]
    stonecounter+=1
    stop=0
    while stop==0:
        if (sand[0],sand[1]+1) not in map.keys():
            sand[1]+=1
        elif (sand[0]-1,sand[1]+1) not in map.keys():
            sand[0]-=1
            sand[1]+=1
        elif (sand[0]+1,sand[1]+1) not in map.keys():
            sand[0]+=1
            sand[1]+=1
        else: 
            map[sand[0],sand[1]]='s'
            stop=1
        if sand[1]>ymax: 
            run=0
            stop=1
    #printmap()    
    #print()
print('Answer 1:',stonecounter)



for t in range(xmin-1000,xmax+1001):
    map[(t,ymax+2)]='r'

#printmap()

run=1
while run==1:
    sand=[500,0]
    stonecounter+=1
    stop=0
    while stop==0:
        if (500,0) in map.keys():
            stop=1
            run=0
            break
        if (sand[0],sand[1]+1) not in map.keys():
            sand[1]+=1
        elif (sand[0]-1,sand[1]+1) not in map.keys():
            sand[0]-=1
            sand[1]+=1
        elif (sand[0]+1,sand[1]+1) not in map.keys():
            sand[0]+=1
            sand[1]+=1
        else: 
            map[sand[0],sand[1]]='s'
            stop=1
printmap()    
    #print()
print('Answer 2:',stonecounter-1)
