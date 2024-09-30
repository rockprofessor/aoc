import numpy as np
import copy

M = [i.strip() for i in open('18.in')]

for l in range(len(M)):
  M[l] = list(M[l])

M = np.array(M)

rows = len(M)
col = len(M[0])


def look(pos):
  dr = [-1, -1, -1,  0,  0,  1,  1,  1]
  dc = [-1,  0,  1, -1,  1, -1,  0,  1]
  count = 0
  for d in range(8):
    if 0 <= pos[0] + dr[d] < rows and 0 <= pos[1] + dc[d] < col:
      r = pos[0] + dr[d]
      c = pos[1] + dc[d]
      if M[r][c] == '#' : count += 1
  return (count)

for k in range(100):
  #part 2
  #M[0][0] = '#'
  #M[rows-1][0] = '#'
  #M[0][col-1] = '#'
  #M[rows-1][col-1] = '#'

  N = copy.deepcopy(M)

  for R in range(rows):
    for C in range(col):
      neighb = look((R,C))
      if M[R][C] == '#':
        if 1 < neighb < 4:
          N[R][C] = '#'
        else:
          N[R][C] = '.'
      else:
        if neighb == 3:
          N[R][C] = '#'
        else:
          N[R][C] = '.'
  M = copy.deepcopy(N)


#part 2
#M[0][0] = '#'
#M[rows-1][0] = '#'
#M[0][col-1] = '#'
#M[rows-1][col-1] = '#'

count = 0
for i in M:
  for j in i:
    if j == '#': count += 1
print('Answer:',count)




