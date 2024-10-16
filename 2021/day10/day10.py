data = [i.strip() for i in open('day10.in')]

br = {')':'(',
      '}':'{',
      ']':'[',
      '>':'<'}

points = {')': 3 ,
          ']': 57,
          '}': 1197,
          '>': 25137}

cpoints = {'(': 1,
           '[': 2,
           '{': 3,
           '<': 4}

score = 0
comp = []
for line in data:
  okay = True
  open = []
  for k in line:
    if k in ['(','{','[','<']:
      open.append(k)
    if k in [')','}',']','>']:
      if br[k] == open[-1]: open.pop()
      else:
        okay = False
        score += points[k]
        break
  if okay:
    open.reverse()
    tot = 0
    for i in open: tot = tot*5 + cpoints[i]
    comp.append(tot)
print('Answer 1:',score)

comp.sort()
print('Answer 2:', comp[len(comp)//2])
