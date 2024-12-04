data = [i.strip() for i in open('4.in')]
    
ans1 = 0    
ans2 = 0
for l in range(len(data)):
    for c in range(len(data[0])):
        if data[l][c] == 'X':
            for dl, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),(-1, 1), (-1, -1)]:
                if 0 <= l + 3*dl < len(data) and 0 <= c + 3*dc < len(data[0]):
                    if data[l+dl][c+dc] + data[l+2*dl][c+2*dc] + data[l+3*dl][c+3*dc] == 'MAS':
                        ans1 += 1

        if data[l][c] == 'A':
            if 0 < l < (len(data) - 1) and 0 < c < (len(data[0]) - 1):
                cross = data[l-1][c-1] + data[l+1][c-1] + data[l-1][c+1] + data[l+1][c+1]
                if cross in ['MMSS', 'SSMM', 'SMSM', 'MSMS']:
                    ans2 += 1

print('Answer 1:', ans1)
print('Answer 2:', ans2)
    
