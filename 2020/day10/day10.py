import math
data = [i.strip() for i in open('day10.in')]

for i in range(len(data)):
    data[i] = int(data[i])

one = 1
three = 1

data.sort()


for i in range(0,len(data)-1):
    if data[i+1] == data[i] +1: one +=1
    if data[i+1] == data[i] +3: three +=1
print('Answer 1:',one * three)

#part 2
data = [0] + data + [max(data) + 3]
z = []
count = 1

for t in range(len(data)-1):
    if data[t+1] - data[t] == 1:
        count += 1
    else: 
        if count > 2: z.append(count)
        count = 1

tripple = z.count(3)
quads = z.count(4)
fives = z.count(5)

print('Answer 2:',pow(2,z.count(3)) * pow(4,z.count(4)) * pow(7,z.count(5)))
