from functools import lru_cache

data = open('19.in').read().strip()
patterns, designs = data.split('\n\n')
patterns = patterns.split(', ')
designs = designs.split()

maxpattern = max(map(len,patterns))

@lru_cache(maxsize = None)
def match(des):
    if des == '': return True
    for i in range(min(maxpattern, len(des)) + 1):
        if des[:i] in patterns and match(des[i:]):
            return True
    return False

@lru_cache(maxsize = None)
def count(des):
    if des == '': return 1
    c = 0
    for i in range(min(maxpattern, len(des)) + 1):
        if des[:i] in patterns:
            c += count(des[i:])
    return c

ans1 = 0
ans2 = 0

for d in designs:
    if match(d):
        ans1 += 1
    ans2 += count(d)

print('Answer 1:', ans1)
print('Answer 2:', ans2)


