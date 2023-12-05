#Checking a massive number of seeds; the program may take a couple minutes
import sys  #for sys.maxsize starting nearest location
import time

start_time = time.time()
seeds = {}
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
                line = line.split()[1:]
                for i, s in enumerate(line):
                    if not i % 2:
                        seeds[s] = line[i+1]
            else:
                mapType += 1

seedcnt = 0
for strtSeed, rnge in seeds.items():
    for seed in range(int(strtSeed), int(strtSeed) + int(rnge)):
        seedcnt += 1
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
print(f'computed {seedcnt} seeds in {time.time() - start_time} seconds')
    