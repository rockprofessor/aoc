import itertools
data = [i.strip() for i in open('day13.in')]

def score(look):
    score = 0
    for i in range(len(look)):
        score += guide[look[i]][look[(i + 1)%len(look)]]
        score += guide[look[i]][look[i - 1]]
    return score

guide = {}
for line in data:
    word = line.split(' ')
    if word[2] == 'gain': h = int(word[3])
    else: h = -int(word[3])
    if word[0] not in guide:
        guide[word[0]] = {}
    guide[word[0]][word[10][:-1]] = h

best = 0
plan = [i for i in guide.keys()]
result = [score(i) for i in itertools.permutations(plan)]

print('Answer 1:',max(result))

guide['me'] = {}
for i in plan:
    guide['me'][i] = 0
    guide[i]['me'] = 0

best = 0
plan = [i for i in guide.keys()]
result = [score(i) for i in itertools.permutations(plan)]
print('Answer 2:',max(result))
