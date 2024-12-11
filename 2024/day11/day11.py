from functools import lru_cache

stones = open('11.in').read().strip()
stones = [int(i) for i in stones.split()]

@lru_cache(maxsize=None)
def cut(s, g):
    g += 1
    if g == 76:
        return 1
    if s == 0: return cut(1, g)
    if len(str(s)) % 2 == 0:
        left = int(str(s)[:len(str(s))//2])
        right = int(str(s)[len(str(s))//2:])
        return cut(left, g) +  cut(right, g)
    return cut(s * 2024, g)

ans1 = 0
for s in stones:
    ans1 += cut(s,0)
print(ans1)
