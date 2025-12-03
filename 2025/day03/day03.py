data = [i.strip() for i in open('3.in')]

grid = []
for line in data:
    grid.append([int(i) for i in line])

c1 = 0

for bank in grid:
    cut = bank[:-1]
    first = max(cut)
    rest = bank[cut.index(max(cut)) + 1:]
    second = max(rest)
    c1 += first * 10 + second

print('Answer 1:', c1)


l = len(grid[0])
c2 = 0

for bank in grid:
    kill = l - 12
    erg = []
    i = 0

    while len(erg) + kill < len(bank) and len(erg) < 12:
        if bank[i] < max(bank[i + 1 : i + kill + 1]):
            m = max(bank[i + 1 : i + kill + 1])
            erg.append(m)
            ind = bank[i + 1 : i + kill + 1].index(m)
            kill -= ind + 1
            i += ind + 2
        else: 
            erg.append(bank[i])
            i += 1
        if kill == 0:
            while len(erg) < 12:
                erg.append(bank[i])
                i += 1

    c2 += int(''.join([str(i) for i in erg]))

print('Answer 2:', c2)
