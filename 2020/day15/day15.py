data = [0, 14, 1, 3, 7, 9]
spoken = {}

for i, x in enumerate(data):
    spoken[x] = i

for i in range(30000000 - len(data)):
    if i == 2014:
        print('Answer 1:', data[-1])

    if data[-1] in spoken:
        data.append(len(data) - spoken[data[-1]] - 1)
    else:
        data.append(0)
    spoken[data[-2]] = len(data) - 2
print('Answer 2:', data[-1])
