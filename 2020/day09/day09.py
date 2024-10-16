data = [i.strip() for i in open('day9.in')]

for i in range(len(data)):
    data[i] = int(data[i])

#pos = 5              #test.in
#p = 5

pos = 25               #day9.in
p=25

for t in range(len(data)-pos):
    found = False
    for i in range(pos-p,pos-1):
        for j in range(i+1,pos):
            if data[i]+data[j] == data[pos]:
                found = True
                break
        if found == True: break
    if found == False:
        print('Answer 1:',data[pos])
        result = data[pos]
        break
    pos +=1

#part 2
for g in range(0, pos-1):
    sum = 0
    while sum < result:
        for h in range(g,pos):
            sum += data[h]
            if sum == result:
                print('Answer 2:',max(data[g:h+1])+min(data[g:h+1]))
                break

