from itertools import combinations
import sympy as sp
import pulp

machines = [line.split() for line in [i.strip() for i in open('10.in')]]

def xor(a,b):
    erg = []
    for i in range(len(a)):
        if a[i] == b[i]:
            erg.append(0)
        else: 
            erg.append(1)
    return erg

ans = 0
ans2 = 0
for m in machines:
    ind = m.pop(0)[1 : -1]
    buttons = m[: -1]
    jolt = eval('[' + m[-1][1:-1] + ']')
    B = []
    combos = []

    indi = []
    for i in range(len(ind)):
        if ind[i] == '.':
            indi.append(0)
        else:
            indi.append(1)

    state = [0  for _ in range(len(indi))]

    for b in buttons:
        B.append(eval('[' + b[1 : -1] + ']'))
        combos = []

    for but in B: 
        c = []
        for i in range(len(ind)):
            if i in but:
                c.append(1)
            else:
                c.append(0)
        combos.append(c)

    k = 1
    found = False
    while not found:
        for t in combinations(range(len(combos)), k):
            erg = state
            for i in t:
                erg = xor(erg, combos[i])
            if erg == indi:
                found = True
                break
        k += 1
    ans += k - 1

    B = sp.Matrix(combos)
    A = B.T
    y = sp.Matrix(jolt)

    n = A.shape[1]
    prob = pulp.LpProblem("MinSumSolution", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(n)]
    prob += pulp.lpSum(x)

    for i in range(A.shape[0]):
        prob += pulp.lpSum(A[i, j]*x[j] for j in range(n)) == y[i]
    prob.solve()

    solution = [pulp.value(xi) for xi in x]
    ans2 += int(sum(solution))

print('Answer 1:', ans)
print('Answer 2:', ans2)
