import re

r_max = 12
g_max = 13
b_max = 14
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


tot = 0
for i, game in enumerate(games):
    imp = 0
    for trial in game:
        if ('red' in trial and trial['red'] > r_max) or ('blue' in trial and trial['blue'] > b_max) or ('green' in trial and trial['green'] > g_max):
            imp = 1
    if not imp:
        tot += i+1

print(tot)
