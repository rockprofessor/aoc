from graphviz import Digraph
dot = Digraph(format='png')
dot.format = 'svg'

data = open('t2.in').read().strip()
inp, gat =data.split('\n\n')

inp = inp.split('\n')
gates = gat.split('\n')

inputs = {} 
for i in inp:
    a, b = i.split(': ')
    inputs[a] = int(b)

while gates:
    for g, gat in enumerate(gates):
        a, out = gat.split(' -> ')
        x, gate, y = a.split(' ')

        dot.node(x, shape = 'ellipse')
        dot.node(y, shape = 'ellipse')
        dot.node('G' + str(g), gate, shape='box')
        dot.node(out, shape='ellipse')
        dot.edge(x, 'G' + str(g))
        dot.edge(y, 'G' + str(g))
        dot.edge(out, 'G' + str(g))

        if x in inputs and y in inputs:
            if gate == 'AND':
                if inputs[x] == 1 and inputs[y] == 1: inputs[out] = 1
                else: inputs[out] = 0
            if gate == 'OR':
                if inputs[x] == 1 or inputs[y] == 1: inputs[out] = 1
                else: inputs[out] = 0
            if gate == 'XOR':
                if inputs[x] != inputs[y]: inputs[out] = 1
                else: inputs[out] = 0
            gates.pop(g)
            break

ans1 = 0
for inp in inputs:
    if inp[0] == 'z': ans1 += inputs[inp] * 2 ** int(inp[1:])
print('Answer 1:', ans1)

x = y = z = 0
for inp in inputs:
    if inp[0] == 'x': x += inputs[inp] * 2 ** int(inp[1:])
    if inp[0] == 'y': y += inputs[inp] * 2 ** int(inp[1:])
    if inp[0] == 'z': z += inputs[inp] * 2 ** int(inp[1:])
print(x,y,z)





# Render and visualize the graph
dot.render('logic_gates_graph', cleanup=True)  # Saves as 'logic_gates_graph.png'
dot.view()

