import re
data = open('3.in').read().strip()

ans1 = 0
ans2 = 0

m = True

matches = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', data)
for match in matches:
    if match == 'do()':
        m = True
    elif match == 'don\'t()':
        m = False
    else:
        t = match[4 : -1]
        a, b = t.split(',')
        if m:
            ans2 += int(a) * int(b)
        ans1 += int(a) * int(b)
  
print('Answer 1:', ans1)                    
print('Answer 2:', ans2)
