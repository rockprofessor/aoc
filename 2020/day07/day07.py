data = [i.strip() for i in open('day7.in')]

def drinnen(inside, outside):
    if inside in bags[outside]:
            return True    
    return any([drinnen(inside, b) for b in bags[outside]])

def count(color):
    return sum([bags[color][b] * (1 + count(b)) for b in bags[color]])

bags = {}
for line in data:
    words = line.split(' ')
    out_bag = words[0]+' '+words[1]  
    in_bag = ' '.join(words[4:]).split(',')
    for i in in_bag:
        if not 'no other bags' in i:
            x = i.strip().split(' ')
            if out_bag not in bags: bags[out_bag] = {}
            bags[out_bag][x[1]+' '+x[2]] = int(x[0])
        else:
            bags[out_bag] = {}

print('Answer 1:',sum([drinnen('shiny gold', bag) for bag in bags]))
print('Answer 2:',count('shiny gold'))
