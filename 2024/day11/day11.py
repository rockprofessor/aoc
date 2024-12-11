from functools import lru_cache

stones = open('11.in').read().strip()
stones = [int(i) for i in stones.split()]

@lru_cache(maxsize=None)
def cut(s, g, b):
    g += 1
    if g > b:  
        return 1
    if s == 0: return cut(1, g, b)
    if len(str(s)) % 2 == 0:
        left = int(str(s)[:len(str(s))//2])
        right = int(str(s)[len(str(s))//2:])
        return cut(left, g, b) +  cut(right, g, b)
    return cut(s * 2024, g, b)

print('Answer 1:', sum(cut(s, 0, 25) for s in stones))
print('Answer 2:', sum(cut(s, 0, 75) for s in stones))
