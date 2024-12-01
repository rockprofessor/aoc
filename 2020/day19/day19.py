rules, data = open('t.in').read().split('\n\n')

rules = {int(x): y for x,y in [r.split(': ') for r in rules.split('\n')]}
data = data.split('\n')[:-1]

for r in rules:
    print(r, ': ', rules[r])
print()

for d in data:

    print(d)

print('test')
print('hey')
print()
