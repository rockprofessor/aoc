input = [i.strip() for i in open('18.in')]
R = 71
start = (0, 0)
finish = (R - 1, R - 1)

data = []
#for n in range(1024): #part 1
for n in range(2959):
    new = [int(i) for i in input[n].split(',')]
    data.append(new)
print('Answer 2:', data[2958])

corrupt = set()
for d in data:
    corrupt.add((d[0], d[1]))  

def look(p):
    new = []
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]: 
        if 0 <= p[0] + dx < R and 0 <= p[1] + dy < R:
            if (p[0] + dx, p[1] + dy) not in corrupt and (p[0] + dx, p[1] + dy) not in visited:
                new.append((p[0] + dx, p[1] + dy))
    return new

curr = [start]
visited = set(start)
step = 0
while finish not in curr or curr == []:
    newcurr = []
    while curr:
        c = curr.pop(0)
        newcurr += look(c)
    while newcurr:
        c = newcurr.pop(0)
        visited.add(c)
        curr.append(c)
        curr = list(set(curr))
    step += 1
print('Answer 1:', step)

