def get_keys_from_value(d, val):
        return [k for k, v in d.items() if v == val]

data = [i.strip() for i in open('day4.in')]

datasort=[]
for x in data:
    a,b=x.split('] ')
    a=a[1:]
    year,month,a=a.split('-')
    day,a=a.split(' ')
    hour,minute=a.split(':')
    datasort.append([int(year),int(month),int(day),int(hour),int(minute),b])
datasort.sort()

times={}
sleep=0
nr=9999
sleepstart=0
guardtimes=[]
for x in datasort:
    if x[5][0]=='G':
        if nr in times.keys():
            times[nr]+=sleep
        else: times[nr]=sleep
        k,nr,m,n=x[5].split(' ')
        nr=int(nr[1:])
        sleep=0
    if x[5][0]=='f':
        sleepstart=x[4]
        guardtimes.append([nr,x[4]])
    if x[5][0]=='w':
        sleep+=x[4]-int(sleepstart)
        guardtimes[-1].append(x[4]-1)
times[nr]+=sleep

max=max(times.values())
keys = get_keys_from_value(times, max)
guard=keys[0]
badguard=[]
for i in guardtimes:
    if i[0]==guard: badguard.append(i)



minutenmax=0
z=0
for i in range(1,60):
    time=0
    for j in badguard:
        if j[1]<=i and i<=j[2]:
            time+=1
    if time>minutenmax:
        minutenmax=time
        z=i
print('Answer 1:',z*guard)

totals={}
for i in range(1,60):
    time=0
    for j in guardtimes:
        if j[1]<=i and i<=j[2]:
            if j[0] not in totals.keys():
                totals[j[0]]={}
            if i in totals[j[0]].keys():
                totals[j[0]][i]+=1
            else: totals[j[0]][i]=1


#for h in totals:
#  print(h)
#  print(totals[h].values())

    #max1=max(totals[h].values())
    #max1 = max(totals[h], key=totals[h].get)
    #print("Maximum value:",max1)
    #keys = get_keys_from_value(totals[h], max1)
#print(keys)
print(totals[163])
print(totals[163].values())

#guard 163
#miunte 35
#Answer 2: 163*35=5705
