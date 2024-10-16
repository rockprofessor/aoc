data = [i.strip() for i in open('day18.in')]

def no_par1(expr):
    part = expr.split(' ')
    x = ''
    op = ''
    for i in part:
        if x and op:
            x = str(eval(x + op + i))
            op = ''
        elif i.isdigit() == True: x = i
        elif i.isdigit() == False: op = i
    return x

sum1 = 0
for line in data:
    while '(' in line:
        s = ''
        for c in line:
            if c != ')':
                if c == '(': s = ''
                else: s += c
            else: 
                line = line.replace('('+s+')',str(no_par1(s)))
    sum1 += int(no_par1(line))
print('Answer 1:', sum1)

#part 2
def no_par2(e):
    expr = e.split(' ')
    while '+' in expr:
        for i in range(len(expr)):
            if expr[i] == '+': 
                g = int(expr[i-1]) + int(expr[i+1])      
                del expr[i-1:i+1]
                expr[i-1] = str(g)
                break
    return str(eval(''.join(expr)))

sum2 = 0
for line in data:
    while '(' in line:
        s = ''
        for c in line:
            if c != ')':
                if c == '(': s = ''
                else: s += c
            
            else: 
                line = line.replace('('+s+')',str(no_par2(s)))
    sum2 += int(no_par2(line))

print('Answer 2:', sum2)
