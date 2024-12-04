d = [i.strip() for i in open('4.in')]

ans1 = 0
ans2 = 0
r = len(d)
for l in range(r):
    for c in range(r):
        if d[l][c] == 'X':
            for dl, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(-1, 1), (-1, -1)]:
                if 0 <= l+3*dl < r and 0 <= c+3*dc < r and d[l+dl][c+dc]+d[l+2*dl][c+2*dc]+d[l+3*dl][c+3*dc] == 'MAS':
                        ans1 += 1

        if d[l][c] == 'A':
            if 0 < l < (r - 1) and 0 < c < (r - 1):
                if d[l-1][c-1] + d[l+1][c-1] + d[l-1][c+1] + d[l+1][c+1] in ['MMSS', 'SSMM', 'SMSM', 'MSMS']:
                    ans2 += 1

print('Answer 1:', ans1)
print('Answer 2:', ans2)
