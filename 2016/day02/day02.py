data = [i.strip() for i in open('day2.in')]

pad1 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
pos = [0, 0]
code = ''
for line in data:
  for i in line:
    if i == 'R':
      if pos[0] < 1: pos[0] += 1
    if i == 'L':
      if pos[0] > -1: pos[0] -= 1
    if i == 'U':
      if pos[1] < 1: pos[1] += 1
    if i == 'D':
      if pos[1] > -1: pos[1] -= 1
  code += str(pad1[pos[1] + 1][pos[0] + 1])
print('Answer 1:', code)

pad2 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 'D', 0, 0, 0],
        [0, 0, 'A', 'B', 'C', 0, 0], [0, 5, 6, 7, 8, 9, 0],
        [0, 0, 2, 3, 4, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

pos = [3, 1]
code = ''
for j in range(0, len(data)):
  for i in range(0, len(data[j])):
    if data[j][i] == 'R':
      if pad2[pos[0]][pos[1] + 1] != 0: pos[1] += 1
    if data[j][i] == 'L':
      if pad2[pos[0]][pos[1] - 1] != 0: pos[1] -= 1
    if data[j][i] == 'U':
      if pad2[pos[0] + 1][pos[1]] != 0: pos[0] += 1
    if data[j][i] == 'D':
      if pad2[pos[0] - 1][pos[1]] != 0: pos[0] -= 1
  code += str(pad2[pos[0]][pos[1]])
print('Answer 2:', code)

