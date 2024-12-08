from itertools import product
data = [i.strip() for i in open('t.in')]

def gen3(l): return [''.join(map(str, digits)) for digits in product(range(3), repeat=l)]
def gen2(l): return [''.join(map(str, digits)) for digits in product(range(2), repeat=l)]

ans = 0
for line in data:
    tv, a = line.split(': ')
    a = a.split()
    a = [int(x) for x in a]
    tv = int(tv)
    #operations = gen2(len(a) - 1)  #part 1
    operations = gen3(len(a) - 1)   #part 2
    for op in operations: 
        erg = a[0]
        for i in range(1, len(a)):
            if op[i - 1] == '0':
                erg += a[i]
            elif op[i - 1] == '1':
                erg *= a[i]
            else:
                erg = int(str(erg) + str(a[i]))
            if erg > tv:
                break
        if erg == tv:
            ans += erg 
            break

print('Answer:', ans)

