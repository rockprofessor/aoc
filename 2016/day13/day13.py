import numpy as np

fav = 1352
end = (31,39)
max = 100

#fav = 10
#end = (7,4)
#max = 10

start = (1,1)

def calc(x,y):
  b = str(bin((x*x + 3*x + 2*x*y + y + y*y)+fav)[2:])
  sum = 0
  for i in b:
    if int(i): sum += 1
  if sum%2 == 1: return '#'
  else: return '.'
    
def printmap(m):
  for y in range(max):
    line = ''
    for x in range(max):
      if (x,y) in visited: line += 'o'
      else: line += map[y][x]
    print(line)

def look(p):
  free = []
  dx = (0,0,-1,1)
  dy = (-1,1,0,0)
  for i in range(4):
    if p[0] + dx[i] >= 0 and p[1] + dy[i] >= 0:
      if map[p[1]+dy[i]][p[0]+dx[i]] == '.' and (p[0]+dx[i],p[1]+dy[i]) not in visited:
        free.append((p[0]+dx[i],p[1]+dy[i]))
  return free
  
map = []
visited = [start]
for x in range(max):
  row = []
  for y in range(max):
    row.append(0)
  map.append(row)  
for x in range(max):
  for y in range(max):
    map[y][x] = calc(x,y)
map = np.array(map)

curr = [start]
steps = 0
while end not in visited:
  new = []
  steps += 1
  
  for c in curr:
    new += look(c)
  
  curr = []
  for t in set(new):
    if t not in visited:
      curr.append(t)
  visited += set(new)
  if steps == 50: print('Answer 2:',len(visited))
  if end in visited: break

print('Answer 1:',steps)


  
