data = [i.strip() for i in open('2.in')]

def check(a):
    y = [a[i+1] - a[i] for i in range(len(a) - 1)]
    if (min(y) > 0 and max(y) < 4) or (min(y) > -4 and max(y) < 0):
        return 1
    return 0

ans1 = 0
ans2 = 0

for d in data:
    x = [int(i) for i in d.split()]
    ans1 += check(x)

    for i in range(len(x)):
        z = x[:i] + x[i+1:]
        if check(z) == 1:
            ans2 +=1
            break
    
print('Answer 1:', ans1)
print('Answer 2:', ans2)
