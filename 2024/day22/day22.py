data = [i.strip() for i in open('22.in')]
data = [int(i) for i in data]

def new(sn):
    sn ^= sn * 64
    sn %= 16777216
    sn ^= sn // 32 
    sn %= 16777216
    sn ^= sn * 2048
    sn %= 16777216
    return sn 

ans1 = ans2 = 0
for x in data:
    for i in range(2000):
        x = new(x)
    ans1 += x
print('Answer 1:', ans1)

seq1 = {}
for x in data:
    price = []
    for _ in range(2000):
        x = new(x)
        price.append(x % 10)

    tested = set()
    for i in range(len(price) - 4):
        seq = (price[i+1]-price[i], price[i+2]-price[i+1], price[i+3]-price[i+2], price[i+4]-price[i+3])
        if seq in tested:
            continue
        tested.add(seq)
        if seq not in seq1:
            seq1[seq] = 0
        seq1[seq] += price[i+4]

print('Answer 2:', max(seq1.values()))


