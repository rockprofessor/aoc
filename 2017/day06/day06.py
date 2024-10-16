mem = open('day6.in').read().strip()
mem = [int(x) for x in mem.split(' ')]

hist = []

while tuple(mem) not in hist:
    hist.append(tuple(mem))
    ind = mem.index(max(mem))
    val = mem[ind]
    mem[ind] = 0
    for i in range(ind+1,ind+val+1):
        mem[i%len(mem)] += 1

print('Answer 1:', len(hist))
print('Answer 2:', len(hist)-hist.index(tuple(mem)))
