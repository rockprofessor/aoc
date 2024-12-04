data = [i.strip() for i in open('4.in')]
    
ans1 = 0    
ans2 = 0
r = len(data)
for l in range(r):
    for c in range(r):
        if data[l][c] == 'X':
            for dl, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(-1, 1), (-1, -1)]:
                if 0 <= l + 3 * dl < r and 0 <= c + 3 * dc < r:
                    if data[l+dl][c+dc] + data[l+2*dl][c+2*dc] + data[l+3*dl][c+3*dc] == 'MAS':
                        ans1 += 1

        if data[l][c] == 'A':
            if 0 < l < (r - 1) and 0 < c < (r - 1):
                cross = data[l-1][c-1] + data[l+1][c-1] + data[l-1][c+1] + data[l+1][c+1]
                if cross in ['MMSS', 'SSMM', 'SMSM', 'MSMS']:
                    ans2 += 1

print('Answer 1:', ans1)
print('Answer 2:', ans2)
    
