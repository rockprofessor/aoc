data = [i.strip() for i in open('day1.in')]
fuel1 = 0
fuel2 = 0

for r in data:
    fuel1 += int(r)//3-2
    totals = int(r)//3-2
    a = totals
    while a > 0:
        a = a//3-2
        if a > 0: totals+=a
    fuel2 += totals
print('Answer 1:', fuel1)
print('Answer 2:', fuel2)
