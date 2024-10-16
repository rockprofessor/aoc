data = [i.strip() for i in open('day8.in')]

input = []
output = []

for line in data:
  a,b = line.split(' | ')
  a = a.split()
  b = b.split()
  a.sort(key = len)
  input.append(a) 
  output.append(b)

count = 0
for x in output:
  for y in x:
    if len(y) in [2,3,4,7]:
        count += 1

print('Answer 1:',count)

#part 2 ***************************

def clear(l,c):
  for z in range(len(l)):
    if c in l[z]: 
      l[z] = l[z].replace(c,'')

sum = 0
for z in range(len(input)):
  line = input[z]
  out = output[z]
  code = {'a':'','b':'','c':'','d':'','e':'','f':'','g':''}

  code['c'] = line[0]
  code['f'] = line[0]

  for r in line[0]:
    line[1] = line[1].replace(r,'')
    line[2] = line[2].replace(r,'')
  code['a'] = line[1]

  for r in line[2]:
    if r in line[3] and r in line[4] and r in line[5]:
      code['d'] = r
      line[2] = line[2].replace(r,'')
      code['b'] = line[2]

  clear(line,code['a'])
  clear(line,code['b'])
  clear(line,code['d'])

  g= line[3]+line[4]+line[5]+line[6]+line[7]+line[8]
  for t in g:
    if g.count(t) == 6: code['g'] = t
    if g.count(t) == 5: code['f'] = t
    if g.count(t) == 4: code['c'] = t
    if g.count(t) == 3: code['e'] = t

  code = {v: k for k, v in code.items()}  #swap key <-> value

  result = ''
  for h in out:
    number = ''
    for g in h:
      number =  number + code[g]
    number = ''.join(sorted(number))

    if number == 'abcefg':   result = result + '0'  
    if number == 'cf':       result = result + '1'
    if number == 'acdeg':    result = result + '2'
    if number == 'acdfg':    result = result + '3'
    if number == 'bcdf':     result = result + '4'
    if number == 'abdfg':    result = result + '5'
    if number == 'abdefg':   result = result + '6'
    if number == 'acf':      result = result + '7'
    if number == 'abcdefg':  result = result + '8'
    if number == 'abcdfg':   result = result + '9'

  sum += int(result)

print('Answer 2:',sum)
