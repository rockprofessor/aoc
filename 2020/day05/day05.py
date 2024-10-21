import math
data = [i.strip() for i in open('day5.in')]
ids = []
for line in data:
    row=0
    column=0
    id=0
    for i in range(0,7):
        if line[i] == 'B': row += int(math.pow(2, 6-i))
    for i in range(7,10):
        if line[i] == 'R' : column += int(math.pow(2, 9-i))
    id = row*8+column
    ids.append(id)
print('Answer 1:', max(ids))

for f in range(min(ids),max(ids) + 1):
    if f not in ids:
        print('Answer 2:', f)
