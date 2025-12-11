# (col, row)
data = [tuple(int(x.strip()) for x in line.split(',')) for line in open('9.in')]
grid = []

C = max(int(c) for (c, r) in data) + 1
R = max(int(r) for (c, r) in data) + 1

area_max = 0
for i in range(len(data) - 1):
    for j in range(len(data)):
        area = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
        if area > area_max:
            area_max = area

print('Answer 1:', area_max)

data.append(data[0])
def printgrid():
    for r in range(R + 1):
        line = ''
        for c in range(C + 2):
            if (c, r) in grid:
                line += 'X'
            else:
                line += '.'
        print(line)

for i in range(len(data) - 1):
    (a,b) = data[i]
    (c,d) = data[i + 1]
    grid.append((a, b))
    grid.append((c, d))

    if a == c:
        for k in range(min(b, d) + 1, max(b, d)):
            grid.append((a, k))
    else:
        for k in range(min(a, c) + 1, max(a, c)):
            grid.append((k, b))


# for r in range(1, R + 1):
#     inside = False
#     side = 'n'
#     for c in range(1, C + 1):
#         u = (c, r + 1) in grid
#         d = (c, r - 1) in grid
#         if (c, r) in grid:              # stehen auf X
#             if u and d:                 # cross line
#                 inside = not inside
#             elif u:                     # ecke up
#                 if side == 'n':
#                     side = 'u'
#                 elif side == 'u':
#                     side = 'n'
#                 else:
#                     inside = not inside
# 
#             elif d:   # ecke down
#                 if side == 'n':
#                     side = 'd'
#                 elif side == 'd':
#                     side = 'n'
#                 else:
#                     inside = not inside
#         else:   # stehen auf .
#             if inside:
#                 grid.append((c, r))

area_max = 0

print('Answer 2:', area_max)


