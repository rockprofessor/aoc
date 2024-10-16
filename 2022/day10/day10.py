with open("day10.in", "r") as angabe:
        data = angabe.read().split('\n')
cycle=1
x=1
reg=[0,0]
count=0
pos=[]
while (data!=[]):
#for i in range(0,7):
    com=data.pop(0)

    if com!='noop':
        a,b=com.split(' ')
        b=int(b)
        reg[0]+=b

        x+=reg[1]
        if((cycle+20)%40==0):
            print(cycle,x)
            count+=cycle*x
        pos.append(x)
        cycle+=1
        reg[1]=reg[0]
        reg[0]=0
    if((cycle+20)%40==0):
        print(cycle,x)
        count+=cycle*x

    cycle+=1
    x+=reg[1]
    reg[1]=reg[0]
    reg[0]=0
    pos.append(x)
print('Answer 1:',count)  

print()
pos.append(0)
for i in range(0,6):
    line=''
    for j in range(1,41):
        if j-1==pos[i*40+j-2] or j-1==pos[i*40+j-2]+1 or j-1==pos[i*40+j-2]-1:  
            line+='#' 
        else:
            line+='.'
        #print(j-1,i*40+j-1,pos[i*40+j-1])
    print(line)
