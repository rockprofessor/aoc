import numpy as np
import copy

data = [i.strip() for i in open('test.in')]
for i in  range(len(data)):
    data[i] = list(data[i])

for i in range(len(data)):
    for j in range(len(data[0])):
        data[i][j] = int(data[i][j])

data = np.array(data)

dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

steps = 10
print(data)
print()
for k in range(steps+1):
    new = copy.deepcopy(data)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if new[i][j] == 9: new[i][j] = 0
            else: new[i][j] += 1
    data = copy.deepcopy(new)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                for d in range(9):
                    if 0 <= i+dy[d] < 10 and 0 <= j+dx[d] < 10:
                        if new[i+dy[d]][j+dx[d]] != 0: 
                            if new[i+dy[d]][j+dx[d]] < 9: new[i+dy[d]][j+dx[d]] += 1
                            else: new[i+dy[d]][j+dx[d]] = 0

    data = copy.deepcopy(new)
    print(data)
    print()
