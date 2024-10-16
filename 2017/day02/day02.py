chksum=0
with open('day2.in') as file:
    for line in file:
        max=0
        min=1000
        for word in line.split():
            if int(word)>max: max=int(word)
            if int(word)<min: min=int(word)
        chksum+=max-min
print('Answer 1:',chksum)

chksum=0
with open('day2.in') as file:
    for line in file:
        r=[]
        for word in line.split():
            r.append(int(word))
        r.sort(reverse = True)
        for i in range(len(r)-1):
            for j in range(i+1,len(r)):
                if r[i]%r[j]==0: 
                    chksum+=int(r[i]/r[j])
print('Answer 2:',chksum)
