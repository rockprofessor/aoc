from functools import lru_cache

stones = open('11.in').read().strip()
stones = [int(i) for i in stones.split()]

@lru_cache(maxsize=None)
def cut(s, b):
    if b == 0:  
        return 1
    if s == 0: return cut(1, b - 1)
    if len(str(s)) % 2 == 0:
        left = int(str(s)[:len(str(s))//2])
        right = int(str(s)[len(str(s))//2:])
        return cut(left, b - 1) +  cut(right, b - 1)
    return cut(s * 2024, b - 1)

print('Answer 1:', sum(cut(s, 25) for s in stones))
print('Answer 2:', sum(cut(s, 75) for s in stones))
