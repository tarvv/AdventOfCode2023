import re

games = []
with open('../../../inputs/02', 'r') as f:
    for line in f:
        line = line.partition(':')[2]
        trials = []
        for trial in line.split(';'):
            clrlist = []
            for color in trial.split(','):
                clrlist.append((re.findall(r'[a-z]+', color)[0], int(re.findall(r'[\d]+', color)[0])))
            trials.append(dict(clrlist))
        games.append(trials)

total = 0
for i, game in enumerate(games):
    rmax = 1
    bmax = 1
    gmax = 1
    for trial in game:
        if 'red' in trial and trial['red'] > rmax:
            rmax = trial['red']
        if 'blue' in trial and trial['blue'] > bmax:
            bmax = trial['blue']
        if 'green' in trial and trial['green'] > gmax:
            gmax = trial['green']
    total += rmax * bmax * gmax
print(total)