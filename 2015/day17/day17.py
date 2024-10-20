from itertools import combinations 

data = open('day17.in').read().split()
data = [int(i) for i in data]

def fakt(n):
    if n == 1: return 1
    else: return n * fakt(n - 1)

#liters = 25
liters = 150
count = 0

minimum = len(data)
r = []
count2 = 0
for i in range(2,len(data)+1):
    comb = combinations(data,i)
    for c in comb:
        if sum(c) == liters: 
            count += 1
            if len(c) == minimum: count2 +=1
            if len(c) < minimum:
                count2 = 1
                minimum = len(c)

print('Answer 1:', count)
print('Answer 2:', count2)







