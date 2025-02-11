import copy
file = open('2.in').read().split(',')
data = copy.deepcopy(file)
data = list(map(int, data))
data[1] = 12
data[2] = 2

for j in range(0, len(data)-1,4):
    opcode = data[j]
    in1 = data[j + 1]
    in2 = data[j + 2]
    out = data[j + 3]
    if opcode == 1:
        data[out] = data[in1] + data[in2]
    elif opcode == 2:
        data[out] = data[in1] * data[in2]
    if opcode == 99:
        break
print('Answer 1:', data[0])

#Part2
answer = 0
noun = 0
verb = 0
while answer != 19690720:
    data = copy.deepcopy(file)
    data = list(map(int, data))
    if noun < 99: noun += 1
    else:
        noun = 0
        verb += 1
    data[1] = noun
    data[2] = verb
    for j in range(0, len(data) - 1, 4):
        opcode = data[j]
        in1 = data[j + 1]
        in2 = data[j + 2]
        out = data[j + 3]
        if opcode == 1:
            data[out] = data[in1] + data[in2]
        elif opcode == 2:
            data[out] = data[in1] * data[in2]
        if opcode == 99:
            break
    answer = data[0]
print('Answer 2:', 100 * noun + verb)
