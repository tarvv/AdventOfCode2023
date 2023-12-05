import sys  #for sys.maxsize starting nearest location

seeds = []
mappings = [[],[],[],[],[],[],[]]   #dict of lists for every mapping
mapType = 0
nearest = sys.maxsize
with open('../../../inputs/05', 'r') as f:
    for line in f:
        if line[0].isnumeric():
            line = line.split()
            mappings[mapType-1].append(line)
        elif line != '\n':
            if line.startswith('seeds:'):
                seeds = line.split()[1:]
            else:
                mapType += 1

for seed in seeds:
    src = seed
    for mapping in mappings:
        dest = int(src)
        for srcToDest in mapping:
            if int(src) >= int(srcToDest[1]) and int(src) < (int(srcToDest[1]) + int(srcToDest[2])):
                dest = int(src) + int(srcToDest[0]) - int(srcToDest[1])
        src = dest
    if src < nearest:
        nearest = src
print(nearest)
    