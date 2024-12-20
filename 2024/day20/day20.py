data = [i.strip() for i in open('20.in')]

R = len(data)
track = []

for r in range(R):
    for c in range(R):
        if data[r][c] == '.':
            track.append((r, c))
        elif data[r][c] == 'S':
            track.append((r, c))
            pos = (r, c)
        elif data[r][c] == 'E':
            track.append((r, c))
            end = (r, c)

race = [pos]
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

while pos != end:
    for d in directions:
        new = (pos[0] + d[0], pos[1] + d[1])
        if new in track and new not in race:
            race.append(new)
            pos = race[-1]
            break

ans1 = ans2 = 0

for a in range(len(race) - 1):
    for b in range(a + 102, len(race)):
        A = race[a]
        B = race[b]
        d = abs(A[0] - B[0]) + abs(A[1] - B[1])
        if d == 2:
            ans1 += 1
        if d <= 20 and b - a - d >= 100:
            ans2 += 1

print('Answer 1:', ans1)
print('Answer 2:', ans2) # 285 for testcase

