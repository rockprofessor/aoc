file = [int(x) for x in open('t.in').read().split(',')]

file[1] = 12
file[2] = 2

i = 0
while file[i] != 99:
    cmd = file[i]
    in1 = file[i + 1]
    in2 = file[i + 2]
    out = file[i + 3]

    if cmd == 1: 
        file[out] = file[in1] + file[in2]
        i += 4
    elif cmd == 2: 
        file[out] = file[in1] * file[in2]
        i += 4
    elif cmd == 3:
        continue
    elif cmd == 4:
        continue
print('Answer 1:', file[0])
