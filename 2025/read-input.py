#read line by line
data = [i.strip() for i in open('t.in')]

#read one line
data = open('t.in').read().strip()

#read grid
grid = {(x,y): c for y, row in enumerate(open('t.in')) for x, c in enumerate(row)}

# seeds: 1778931867 1436999653 3684516104
# 
# seed-to-soil map:
# 1965922922 2387203602 59808406
# 2540447436 434094583 220346698
# 2217992666 1677013102 149631368
# 
# soil-to-fertilizer map:
# 974611207 822914672 41736646
# 1617020803 484683369 227984726
# 2936246728 1897199618 22236339
# 
# fertilizer-to-water map:
# 2256462238 272868806 222756596
# 2883874475 1945255196 178320531
# 1025753868 1262393928 220069640
# ...

seeds, *changes = open('5.in').read().split('\n\n')
seeds = list(map(int, seeds.split(":")[1].split()))


