import colorama
from colorama import Fore

import time
data=open('test.in', 'r').read().split('\n')

def printmap():
    for i in range(xmax):
        line=''
        for j in range(ymax):
            if (i,j) in path: 
                line+=Fore.RED+map[i][j]
            elif map[i][j]=='~': line+=Fore.BLUE+map[i][j]
            else: line+=Fore.GREEN+map[i][j]
        print(line)
    print(Fore.WHITE)    

#create map

xmax=len(data)
ymax=len(data[0])
map=[]
for i in range(xmax):
    line=[]
    for j in range(ymax):
        x=data[i][j]  
        if ord(x)<ord('a'):        
            if x=='S': 
                S=[i,j]
                line.append('a')
            else: 
                E=[i,j]
                line.append('z')
        else: line.append(x)
    map.append(line)

path=set()
path.add((S[0],S[1]))
printmap()

count=0
start = time.time()
while (E[0],E[1]) not in path:
    temppath=set()
    for r in path:
        if (r[0]<xmax-1) and ord(map[r[0]+1][r[1]])-ord(map[r[0]][r[1]])<2:     
            temppath.add((r[0]+1,r[1]))
        if (r[0]>0) and ord(map[r[0]-1][r[1]])-ord(map[r[0]][r[1]])<2:     
         temppath.add((r[0]-1,r[1]))
        if (r[1]<ymax-1) and ord(map[r[0]][r[1]+1])-ord(map[r[0]][r[1]])<2:     
            temppath.add((r[0],r[1]+1))
        if (r[1]>0) and ord(map[r[0]][r[1]-1])-ord(map[r[0]][r[1]])<2:     
            temppath.add((r[0],r[1]-1))

    for r in path:
        map[r[0]][r[1]]='~'
        
    count+=1
    path=temppath
    printmap()
end = time.time()
print('time=',round(end - start,3),'s')
print(count)
