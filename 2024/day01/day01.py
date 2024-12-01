data = [i.strip() for i in open('1.in')]
left = []
right = []

for line in data:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

ans1 = 0
ans2 = 0

for i in range(len(left)):
    ans1 += abs(left[i] - right[i])
    ans2 += left[i] * right.count(left[i])

print('Answer 1:', ans1)
print('Answer 2:', ans2)

