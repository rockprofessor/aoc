from sympy import *
data = [i.strip() for i in open('day11.in')]

rounds=10000

monkey=[]
for i in range(0,len(data),7):
    monkeynr=i
    facts=[]
    a,b=data[i+1].split(': ')
    startitem=b.strip().split(', ')
    for k in range(0,len(startitem)):
        startitem[k]=int(startitem[k])
    c,d=data[i+2].split(' old ')
    e,f=d.split(' ')
    if e=='*':
        operation=0  #mal
    else:
        operation=1   #plus
    opsteps=f
    g,test=data[i+3].split('by ')
    test=int(test)
    h,iftrue=data[i+4].split('monkey ')
    iftrue=int(iftrue)
    k,iffalse=data[i+5].split('monkey ')
    iffalse=int(iffalse)
    facts.append(startitem)
    facts.append(operation)
    facts.append(opsteps)
    facts.append(test)
    facts.append(iftrue)
    facts.append(iffalse)
    monkey.append(facts)

ins=[]
for i in range(0,len(monkey)):
    ins.append(0)
fakt=1
for r in monkey:
    fakt*=r[3]
print(fakt)
for z in range(0,rounds):
    for i in range(0,len(monkey)):
        for j in range(0,len(monkey[i][0])):
            ins[i]+=1
            if monkey[i][2]=='old':
                if monkey[i][1]==0:
                    monkey[i][0][j]=pow(monkey[i][0][j],2)
                else:
                    monkey[i][0][j]+=monkey[i][0][j]

            else:
                if monkey[i][1]==0:
                    monkey[i][0][j]*=int(monkey[i][2])
                else:
                    monkey[i][0][j]+=int(monkey[i][2])
            #if int(monkey[i][0][j]/3)%monkey[i][3]==0:
            if monkey[i][0][j]%monkey[i][3]==0:
                monkey[monkey[i][4]][0].append(monkey[i][0][j]%fakt)
                monkey[i][0][j]=0
            else:
                monkey[monkey[i][5]][0].append(monkey[i][0][j]%fakt)
                monkey[i][0][j]=0

        for r in range(0,len(monkey)):
            while 0 in monkey[r][0]:
                monkey[r][0].remove(0)

s=1
print(ins)
max1=max(ins)
ins.remove(max1)
max2=max(ins)
print(max1,max2)
print('Answer 1=',max1*max2)
