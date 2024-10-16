data=[i.strip() for i in open('day2.in')]

chksum=0
doub=0
trip=0
for line in data: 
    doubfound=0
    tripfound=0
    for s in range(ord('a'),ord('z')+1):  #every letter of the alphabet
        if line.count(chr(s))==2: 
            doubfound=1
        if line.count(chr(s))==3: 
            tripfound=1
    doub+=doubfound
    trip+=tripfound

print('Answer 1:',doub*trip)
a=''
b=''
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        diffcount=0
        for z in range(len(data[0])):
            if data[i][z]!=data[j][z]: diffcount+=1
        if diffcount==1:
            a=data[i]
            b=data[j]
            break

r=''
for i in range(len(a)):
    if a[i]==b[i]: r+=(a[i])
print('Answer 2:',r)
