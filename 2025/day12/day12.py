data = open('12.in').read().strip()
data = data.split('\n\n')

regions = data.pop(-1)
regions = regions.split('\n')
shapes =[]

for line in data:
    shapes.append(line.split()[1:])

for shape in shapes:
    for line in shape:
        print(line)
    print()

ans1 = 0
for region in regions:
    count, region = region.split(': ')
    c1, c2 = count.split('x')
    region = [int(x) for x in region.split()]
    if int(c1) * int(c2) >= sum(region) * 9:
        ans1 += 1
print(ans1)
