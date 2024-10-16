data = [x.strip() for x in open('test.in')]
data = [x.replace(',','') for x in data]

def path(x):
    return [x] + (path(revtow[x]) if x in revtow else [])

weights = {}
tower = {}
revtow = {}

for line in data:
    inf = line.split()
    start = inf.pop(0)
    weight = int(inf.pop(0)[1:-1])
    if inf: 
        inf.pop(0)
    weights[start] = weight
    tower[start] = inf

# wege umkehren
for c in tower:
    if c != []:
        for r in tower[c]:
            revtow[r] = c 

# weg bis root gehen
balance = []
for i in revtow:
    balance.append([i] + path(revtow[i]))

# gewicht von Zweigen addieren
for r in balance:
    for s in range(1,len(r)):
        weights[r[s]] += weights[r[s-1]]

#irgendeinen weg zu root gehen
for z in balance:
    root = z[-1]
    break
print('Answer 1:', root)
print()

print('Zweige von root:',root)
for r in revtow:
    if revtow[r] == root:
        print(r,weights[r])

print()
print('tower:')
for t in tower:
    print(t,tower[t])

# print()
# print('revtow:')
# for r in revtow:
#   print(r,revtow[r])

print()
print('balance:')
for b in balance:
    print(b)





print()
print('weights:')
for w in weights:
    print(w,weights[w])


#                 gyxo
#               /     
#          ugml - ebii
#        /      \     
#       |         jptl - abcd - tert
#       |        
#       |         pbga
#      /        /
# tknk --- padx - havc
#      \        \
#       |         qoyq
#       |             
#       |         ktlj
#        \      /     
#          fwft - cntj
#               \     
#                 xhth
