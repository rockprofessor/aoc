spoken = {}

for i, x in enumerate([0, 14, 1, 3, 7]):
    spoken[x] = i

last = 9
for i in range(6, 30000000):
    if i == 2020:
        print('Answer 1:', last)
    secondlast = last
    if last in spoken:
        last = (i - spoken[last] - 1)
    else:
        last = (0)
    spoken[secondlast] = i - 1
print('Answer 2:',last) 
