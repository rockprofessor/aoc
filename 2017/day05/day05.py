import copy
data=[i.strip() for i in open('5.in')]

instr=[]
for t in data:
    instr.append(copy.deepcopy(int(t)))

k=0    #pos in instruction list
exit=0
steps=0
while exit==0:
    if k<len(instr):
        jump=instr[k]
    else: 
        break
    instr[k]+=1
    k+=jump
    steps+=1
print('Answer 1:',steps)

#Part 2

instr=[]
for t in data:
    instr.append(copy.deepcopy(int(t)))

k=0    #pos in instruction list
exit=0
steps=0
while exit==0:
    if k<len(instr):
        jump=instr[k]
    else: 
        break
    if jump>2:
        instr[k]-=1
    else:
        instr[k]+=1
    k+=jump
    steps+=1
print('Answer 2:',steps)
