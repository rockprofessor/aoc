grid = {(x,y): c for y, row in enumerate(open('4.in')) for x, c in enumerate(row)}

m = max(x for x, y in grid)
def look(r, c):
    n = 0
    for (u, s) in {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}:
        if 0 <= r + u < m and 0 <= c + s < m:
            if grid[r + u, c + s] == '@':
                n += 1
    return n

c1 = 0
for C in range(m):
    for R in range(m):
        if grid[C, R] == '@' and look(C, R) < 4:
            c1 += 1

print('Answer 1:', c1)

c2 = 0
go = True
while go:
    kill = []
    for C in range(m):
        for R in range(m):
            if grid[C, R] == '@' and look(C, R) < 4:
                c2 += 1
                kill.append((C,R))
 
    if kill == []:
        go = False
    for (x,y) in kill:
        grid[x,y] = '.'

print('Answer 2:', c2)
