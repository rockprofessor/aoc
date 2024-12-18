def calc(A, B, C, program, part2):
    out = []
    ip = 0

    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]
        if operand < 4:     cop = operand
        elif operand == 4:  cop = A
        elif operand == 5:  cop = B
        elif operand == 6:  cop = C

        if opcode == 0:     A = int((A / 2 ** cop) // 1)
        elif opcode == 1:   B = B ^ operand
        elif opcode == 2:   B = (cop % 8) % 10
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:   B = B ^ C
        elif opcode == 5:
            out.append(cop % 8)
            if out != program[:len(out)] and part2:
                return out
        elif opcode == 6:   B = int((A / 2 ** cop) // 1)
        elif opcode == 7:   C = int((A / 2 ** cop) // 1)
        ip += 2
    return (out)

program = [2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0]
print('Answer 1:', calc(41644071, 0, 0, program, False))

ans2 = 0
#reverse engineering by hand ! then find smallest number that gives the same output
for n in range(190593311094671, 190593310997000, -1):
    if calc(n, 0, 0, program, True) == program:
        ans2 = n

print('Answer 2:', n)
