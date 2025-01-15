import networkx as nx

with open("24.in") as fname:
    starting_values, connections = fname.read().split("\n\n")  # divide the input file into two sections

starting_values = starting_values.splitlines()
connections = connections.splitlines()

statedict = {}  # where we store the state (0 or 1) of each node

for line in starting_values:
    gate, value = line.split(": ")
    statedict[gate] = int(value)

logicmap = {"XOR": "^", "AND": "&", "OR": "|"}

# Graph needs to be directed to find the predecessors
G = nx.DiGraph()

# Create the edges of a graph, storing the type of logic gate as an attribute
for line in connections:
    inputs, output_gate = line.split(" -> ")  # "tgd XOR rvg" "z01"
    input_one, logic, input_two = inputs.split()
    G.add_edge(input_one, output_gate, type=logicmap[logic])
    G.add_edge(input_two, output_gate, type=logicmap[logic])

while not len(statedict) == len(G.nodes()):  # iterate until we have a state for every node
    for node in G.nodes():
        if G.in_degree(node) == 2 and statedict.get(node) is None:  # avoid nodes that don't have 2 inputs (like the starting nodes), avoid nodes that already have a state set
            inputs = []  # there will be two inputs for each node
            for prenode, datadict in G.pred[node].items():  # get the names of the predecessor node in the graph and it's type (contained in datadict)
                inputs.append(prenode)

            # Just select nodes where we know what the two inputs are
            if statedict.get(inputs[0]) is not None and statedict.get(inputs[1]) is not None:  # have to explicitly test None, as 0 evaluates to False
                # use the eval() function to calulate the output of the logic gate
                statedict[node] = eval(str(statedict.get(inputs[0])) + datadict["type"] + str(statedict.get(inputs[1])))
    
    # my input worked through this loop in 43 passes
    print(len(statedict),"/",len(G.nodes()))

# we don't explicitly know how many z nodes there are, so we need to count them
number_of_z_gates = 0
for node in G.nodes():
    if node[0] == "z":  # first letter begins with z
        number_of_z_gates += 1

# create a string of 0s and 1s from the state of z gates in order
binary = ""
for i in range(number_of_z_gates):
    z_node_name = f'z{i:02}'
    binary += str(statedict[z_node_name])

# "binary" is the wrong endian, so we need to reverse it with [::-1] and convert from base 2 to 10 using int()
print("Part 1:", int(binary[::-1], 2))
