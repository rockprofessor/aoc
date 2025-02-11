import copy

file = [int(x) for x in open('2.in').read().split(',')]
file2 = copy.deepcopy(file)

file[1] = 12
file[2] = 2

i = 0
while file[i] != 99:
    cmd = file[i]
    in1 = file[i + 1]
    in2 = file[i + 2]
    out = file[i + 3]
 
    if cmd == 1: file[out] = file[in1] + file[in2]
    elif cmd == 2: file[out] = file[in1] * file[in2]
    i += 4
print('Answer 1:',file[0])

#part 2 *******************************************
answer = 0
noun = 0
verb = 0
while answer != 19690720:
    if noun < 99: noun += 1
    else:
        noun = 0
        verb += 1
    file2[1] = noun
    file2[2] = verb
    i = 0
    while file[i] != 99:
        cmd = file[i]
        in1 = file[i + 1]
        in2 = file[i + 2]
        out = file[i + 3]
        if cmd == 1:
            file2[out] = file2[in1] + file2[in2]
        elif cmd == 2:
            file2[out] = file2[in1] * file2[in2]
    answer = file2[0]

print('Answer 2:', 100 * noun + verb)
print('noun:', noun, 'verb:', verb)
