filesystem={}
path=[]
letters=[]
def printpath():
    pathstr=''
    for i in path:
        pathstr+=i+' '
    print(pathstr)
    
def getpath():
    r=''
    for i in path:
        r+=i
    return(r)

data = [i.strip() for i in open('day7.in')]
for i in range(len(data)):
    word=data[i].strip().split()
    if word[1]=='cd':
        if word[2]=='..': path.pop()
        elif word[2]=='/': 
            path=['/']
            if '/' not in filesystem:
                filesystem['/']=0
        else: 
            path.append(word[2])
            if word[2] not in letters:
                letters.append(word[2])
            if word[2] not in filesystem:
                filesystem[getpath()]=0
    elif word[1]=='ls':

        i+=1
        word=data[i].strip().split()
        while word[0]!='$':
            if word[0]!='dir': 
                filesystem[getpath()]+=int(word[0])
            i+=1
            if i<len(data):
                word=data[i].strip().split()
            else: break


space={}
for j in letters:
    space[j]=0
    for i in filesystem.keys():
        if j in i:
            space[j]+=filesystem[i]

count=0
for h in space:
    #print(h,space.get(h))
    if space.get(h)<=100000:
        count+=space.get(h)
print('Answer 1:',count)


print(filesystem)
